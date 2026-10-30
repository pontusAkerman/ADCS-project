import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_continuous_are
from scipy.linalg import solve_discrete_are, expm
from scipy.optimize import minimize
import sympy as sp
import utility as util
from RWIP_Dynamics import Dynamics
from RWIP_Simconfig import SimConfig as cfg


# ==========================================================================
# Parameter containers
# ==========================================================================

# Class containing all the physical parameters of the system, including the body and wheel mass, length, inertia and gravity.
class PhysicalParams:
    def __init__(self):
        self.m_b: float = 1.0    # body mass [kg]
        self.m_w: float = 1.0    # wheel mass [kg]
        self.h: float = 0.1      # body side length [m]
        self.r_w: float = 0.025  # reaction wheel radius [m]
        self.g: float = 9.82     # gravity [m/s^2]
    
    def m_tot(self):
        return self.m_b + self.m_w  #Total mass of body and wheel
    
    
    def l(self):
        return np.sqrt(2 * self.h**2) / 2   # Length from pivot point to center of body/wheel
    
    
    def I_b(self):
        return (2/3) * self.m_b * self.h**2 # Inertia of the body
    
    
    def I_w_pivot(self):
        return self.m_w * self.l**2 # Inertia of the wheel around the pivot point
    
    
    def I_p(self):
        return self.I_b + self.I_w_pivot    # Inertia around the pivot, total of body and wheel inertia
    
    
    def I_w(self):
        return 0.5 * self.m_w * self.r_w**2 #Inertia of the wheel around its own pivot
    
    
    def mgl(self):
        return self.m_tot * self.g * self.l # Gravity momentum om the body and wheel


# Class with the entire control functionality, including the swing-up, mpc and lqr controllers, as well as the blending function that decides which controller to use when.
class ControlFunctionality:    

    # ==========================================================================
    # Integration
    # ==========================================================================

    def integrate_step(state, u, p, cfg, dt):   # Integration step using Semi-Implicit Euler integration
        """
        Semi-implicit Euler integration.
        
        This is usually a little better than plain Euler for mechanical systems
        
        """
        
        phi, phi_dot, theta, theta_dot = state  # All current system states
        
        xdot = Dynamics.nonlinear_dynamics(state, u, p, tau_d=cfg.tau_d) # State derivatives of the nonlinear system dynamics

        phi_ddot = xdot[1]      # Assign the wheel acceleration
        theta_ddot = xdot[3]    # Assign the error acceleration
        
        # Update velocities first
        phi_dot_next = phi_dot + phi_ddot * dt          # Calculates the predicted next wheel speed based on the current wheel angle and wheel acceleration
        theta_dot_next = theta_dot + theta_ddot * dt    # Calculates the predicted next error rate based on the previous and the current error acceleration
        
        # Update positions using new velocities, using Euler integration
        phi_next = phi + phi_dot_next * dt              # Predicts what the next wheel angle will be using the current wheel angle and current wheel speed
        theta_next = theta + theta_dot_next * dt        # Predicts what the next error will be based on the current error and the error rate
        
        theta_next = util.wrap_angle(theta_next) # Wraps the future predicted error within our set range
        
        return np.array([
            phi_next,
            phi_dot_next,
            theta_next,
            theta_dot_next
        ], dtype=float) # Returns an array of the future predicted states


    # ==========================================================================
    # MPC Controller
    # ==========================================================================

    def build_mpc_controller(p, Q, R, dt):
            """ 
            Here we build the mpc controller, essentially we run this script first to build everything that only needs to be made once.
            
            """
            
            a_mpc = p.mgl / p.I_p
                    
            A = np.array([
                    [0, 1, 0, 0],       # phi
                    [0, 0, -a_mpc, 0],     # phi_dot
                    [0, 0, 0, 1],          # theta
                    [0, 0, a_mpc, 0],      # theta_dot
                ])  # A matrix for the mpc
                    
            B = np.array([
                    [0],
                    [1 / p.I_w + 1 / p.I_p],
                    [0],
                    [-1 /p.I_p],
                ])  # B matrix for the mpc
            
            A_d, B_d = util.discretize_system(A, B, dt)
                    
            P = solve_discrete_are(A_d, B_d, Q, R)    # Solved from the Ricatti equation, current cost of the state the controller is in
                
            
            return A_d, B_d, P


    def cost_function(U, state, N, Q, R, P, p, R_delta_u, u_prev):
        
        # Cost variable
        cost = 0.0
        
        # Reference states 
        x_ref = np.array([
            0.0,
            0.0,
            0.0,
            0.0
        ])
        
        X = np.zeros((N + 1, len(x_ref)))
        X[0] = state
        
        for k in range(N):
            
            # Predict next state 
            X[k+1] = ControlFunctionality.integrate_step(X[k], U[k], p, cfg, cfg.dt_mpc)
            
            w_region = 0.0     # Penalty coefficient, we want the mpc to get to the lqr region
            theta_excess = max(0, util.wrap_angle(X[k+1, 2]) / cfg.theta_bf_min_ml - 1)             # Takes the excess/how far away the current angle is from the ideal angle, within the LQR range.
            theta_dot_excess = 0 #max(0, X[k+1, 3] / cfg.theta_dot_limit - 1)         # Takes the excess/how far away the current angle rate is from the ideal angle rate, within the lqr range.
            
            
            # State error
            e = np.array([
                X[k+1, 0] - x_ref[0],
                X[k+1, 1] - x_ref[1],
                X[k+1, 2] - x_ref[2],
                X[k+1, 3] - x_ref[3]])
            e_n = e #/ x_scale   # Normalizes the error using the scales
            u_n = float(U[k])# / u_scale
            
            if(k == 0):
                du = float(U[k] - u_prev)
            else:
                du = float(U[k] - U[k-1])
                
            # Stage cost
            cost += (
            e_n.T @ Q @ e_n 
            + u_n**2*R 
            + du**2 * R_delta_u # Penalizes rapid changes in torque
            + w_region 
            * (theta_excess**2 
            + theta_dot_excess**2)   # State costs + an added cost telling the MPC that it is far better to be within the range of the LQR than to try being in a good position for the equilibrium
            )
        
        # Terminal cost.
        e_terminal = np.array([
            X[-1, 0] - x_ref[0],
            X[-1, 1] - x_ref[1],
            X[-1, 2] - x_ref[2],
            X[-1, 3] - x_ref[3]])
        e_n_terminal = e_terminal  # Normalized error for comfort when picking cost matrices

        
        cost_info = 0
        
        if cost_info:
            if(U[k] >= cfg.u_max or U[k] <= -cfg.u_max):
                print(
                    f"Phi cost: {e_n[0]**2*Q[0,0]}, "           # Phi cost
                    f"Phi_dot cost: {e_n[1]**2*Q[1,1]}, "       # Phi_dot cost
                    f"Theta cost: {e_n[2]**2*Q[2,2]}, "         # Theta cost
                    f"Theta_dot cost: {e_n[3]**2*Q[3,3]}, "     # Theta_dot cost
                    f"u cost: {(U[k]**2*R).item()}"             # u cost, item() turns an array number into a scalar
                )
                
                print(
                        f"Terminal Phi cost: {e_n_terminal[0]**2*P[0, 0]}, "           # Phi cost
                        f"Terminal Phi_dot cost: {e_n_terminal[1]**2*P[1, 1]}, "       # Phi_dot cost
                        f"Terminal Theta cost: {e_n[2]**2*P[2, 2]}, "         # Theta cost
                        f"Terminal Theta_dot cost: {e_n[3]**2*P[3, 3]}, "     # Theta_dot cost
                        )
        
        return float(cost.item())


    def mpc_controller(state, U_0, P, p, N, u_prev):   #MPC controller
            """
            
            MPC controller:
                Predicts future outcomes and chooses the most ideal 
            
            """
            
            state[2] = util.wrap_angle(state[2])
            
            bounds = [(-cfg.u_max, cfg.u_max)]*N
            
            constraints = {
                'type': 'ineq',
                'fun': util.wheel_speed_constraint,
                'args': (state, N, p, cfg.dt_mpc)
            }
            
            # Optimizer for finding the best control input sequence
            best = minimize(
                ControlFunctionality.cost_function,
                U_0,
                args = (state, N, Q_mpc, R_mpc, P, p, R_delta_u_mpc, u_prev),
                bounds=bounds,
                constraints=constraints,
                method="SLSQP"
            )
            
            
            u_cmd = best.x[-1]   # MPC controller input calculated based on future predictions, only makes the first step of the best sequence
    
            u_cmd = util.apply_wheel_speed_limit(u_cmd, state, cfg.phi_dot_max_rad)
            
            u_cmd = util.clip_torque(u_cmd, cfg.use_torque_limit, cfg.u_max)
            
            U_0 = np.concatenate((best.x[1:], [0.0]))
            
            
            return float(u_cmd), U_0 # Returns the controller input and the next starting guess for the next sequence, to save performance.
    


    # ==========================================================================
    # LQR Controller
    # ==========================================================================

    def build_lqr_controller(p, Q, R):
            """
            Build the linearized LQR controller around upright.
            
            LQR state:
                x_lqr = [theta, theta_dot, phi_dot]
    
            """
            
            a_lqr = p.mgl / p.I_p
            
            A = np.array([
                [0, 1, 0],
                [a_lqr, 0, 0],
                [-a_lqr, 0, 0]
            ])  # A matrix for the lqr
            
            B = np.array([
                [0],
                [-1 /p.I_p],
                [1 / p.I_w + 1 / p.I_p]
            ])  # B matrix for the lqr
            
            P = solve_continuous_are(A, B, Q, R)    # Solved from the Ricatti equation, current cost of the state the controller is in
            
            # K = R^-1 B^t P, but solve is numerically nicer than inverse
            K = np.linalg.solve(R, B.T @ P) # Numerically solved K matrix
            
            return A, B, K, P
    

    def lqr_controller(state, K):   # LQR controller
        """
        LQR controller.
        
        Uses:
            x_lqr = [theta, theta_dot, phi_dot]
        
        """
        
        phi_dot, theta, theta_dot = state[1], state[2], state[3]  # All current system states
        
        theta = util.wrap_angle(theta)   # Wraps the error angle within our set range
        
        x_lqr = np.array([
            theta,
            theta_dot,
            phi_dot
        ])  # Puts all the Useable LQR states in a array
        
        u_cmd = -(K @ x_lqr).item() # Calculates the controller input based on the current state
        
        u_cmd = util.apply_wheel_speed_limit(u_cmd, state, cfg.phi_dot_max_rad)
        
        u_cmd = util.clip_torque(u_cmd, cfg.use_torque_limit, cfg.u_max) # Clip the input signal between the set torque limit
        
        return float(u_cmd) # Returns the controller input


    
    # ==========================================================================
    # Swingup Controller
    # ==========================================================================

    def pendulum_body_energy(theta, theta_dot, p): # Total amount of pendulum energy available
            """
            Body energy relative to upright-angle convention
            
            E = kinetic + potential
            = 1/2 I_p theta_dot^2 + mgl cos(theta)
            
            """
            
            E = 0.5 * p.I_p * theta_dot**2 + p.mgl * (np.cos(theta) + 1)  # Calculates the current energy of the body and wheel based on the current states
            
            
            return E
    

    def swingup_controller(state, p, cfg):  # Swing-up controller
        """
        Energy-based swing-up controller.
        
        Goal:
            E -> E_des
            
        where:
            E_des = mgl
        
        """
        
        # Swing-up controller parameters
        k_E = 0.01  # Coefficient to determine how much torque the swing up controller should respond with at a certain error.

        theta, theta_dot = state[2], state[3]
        
        theta_error = util.wrap_angle(theta)
    
        E = ControlFunctionality.pendulum_body_energy(theta_error, theta_dot, p)  # Total current pendulum energy
        
        E_des = -p.mgl   # Desired pendilum energy to reach the set target
        E_err = E - E_des   # How much energy is required to be added or removed to reach the desired amount of energy
        
        u_cmd = k_E * E_err * theta_dot * np.cos(theta) # Swingup controller input based on the K value, Energy error and error rate
        
        # Always apply the limiters
        u_cmd = util.apply_wheel_speed_limit(u_cmd, state, cfg.phi_dot_max_rad)
        u_cmd = util.clip_torque(u_cmd, cfg)
                
        
        return float(u_cmd)



    # ==========================================================================
    # Control Compliments
    # ==========================================================================

    def execute_controller(state, mode, K, U_0, p, N_mpc, u_mpc, mpc_update, u_prev):  # Deciding which controller is being used where
        """
        Hybrid controller:
            far from upright -> swing-up
            near upright     -> LQR
            
            Uses hysteresis:
                enter LQR at theta_lqr_enter
                exit LQR at theta_lqr_exit
        
        """
        
        theta, theta_dot = state[2], state[3]  # All current system states
        
        # Theta error, this wraps the theta angle between -pi and pi, as the equilibrium is at the top and it can go to either side, but never exceed 180 degrees.
        theta_error = util.wrap_angle(theta)
        
        # Determines omega depending on the range of the blending function, and normalizes it between 0 and 1
        omega_sm = util.smoothstep_function(theta_error, cfg.theta_bf_min_sm, cfg.theta_bf_max_sm)
        
        
        # Calls on the smoothstep function to get the value of omega, between 0 and 1, to help determine which controller should be used
        omega_ml = util.smoothstep_function(theta_error, cfg.theta_bf_min_ml, cfg.theta_bf_max_ml)     
        
        # If omega is at 1, then we are within thhe Swing-up region
        if omega_sm >= 1.0:
            mode = "swing"
            
            # Swing-up Control Input
            u_cmd = ControlFunctionality.swingup_controller(state, p, cfg)
            U_0 = np.zeros([N_mpc])

        # if omega is at 0, then we are within the mpc region
        elif omega_ml <= 0.0:
            mode = "lqr"
            
            u_cmd = ControlFunctionality.lqr_controller(state, K)
                    
            
        # If we are between the mpc and swing-up region, then we are in the blending region and the blending function takes over
        elif omega_sm > 0.0 and omega_sm < 1.0:
            mode = f"blending: {omega_sm:.2f}"
            
            # Recalculates the MPC if its time, otherwise it will continue using the current control input
            if mpc_update:
                
                # MPC Control Input
                u_mpc, U_0 = ControlFunctionality.mpc_controller(state, U_0, P_mpc, p, N_mpc, u_prev)
                    
            # Swing-up Control Input 
            u_swing = ControlFunctionality.swingup_controller(state, p, cfg)
                    
            # Decides how much of each controller input should be used of the MPC or Swing-up
            u_cmd = (1 - omega_sm) * u_mpc + omega_sm * u_swing

            
        elif omega_ml > 0.0:
            mode = f"blending: {omega_ml:.2f}"
            
            # Recalculates the MPC if its time, otherwise it will continue using the current control input
            if mpc_update:
                # MPC Control Input
                u_mpc, U_0 = ControlFunctionality.mpc_controller(state, U_0, P_mpc, p, N_mpc, u_prev) 
                
            # LQR Control Input
            u_lqr = ControlFunctionality.lqr_controller(state, K)
            
            # Decides how much of each controller input should be used of the LQR or MPC
            u_cmd = (1 - omega_ml) * u_lqr + omega_ml * u_mpc
            
        
        else:
            mode = "lqr"
            
            # LQR Control Input
            u_cmd = ControlFunctionality.lqr_controller(state, K)
                               
        
        # Applies both the wheel speed limit and the torque limit for the motor
        u_cmd = util.apply_wheel_speed_limit(u_cmd, state, cfg.phi_dot_max_rad)
        u = util.clip_torque(u_cmd, cfg.use_torque_limit, cfg.u_max) # Clip the input signal between the set torque limit
        
                    
        # returns the initial control guess of the mpc, the current control input, the current mode and the current mpc control input.
        return U_0, u, mode, u_mpc


# ==========================================================================
# Main script
# ==========================================================================

p = PhysicalParams()    # Physical parameters

Q_lqr = np.diag([
    10e-2,      # theta
    10e-1,      # theta_dot
    10e-4       # phi_dot
])  # Cost matrix

Q_mpc = np.diag([
    0.0,            # Phi
    10e-4,           # Phi_dot, wheel has to be spinnin
    10e5,           # Theta
    10e-2           # Theta_dot
]) # Cost matrix used by the MPC

R_lqr = np.array([[10e3]])    

R_mpc = np.array([[10e3]])

R_delta_u_mpc = 1000.0

A_LQR, B_LQR, K, P_lqr = ControlFunctionality.build_lqr_controller(p, Q_lqr, R_lqr)

A_MPC, B_MPC, P_mpc = ControlFunctionality.build_mpc_controller(p, Q_mpc, R_mpc, cfg.dt_mpc)

