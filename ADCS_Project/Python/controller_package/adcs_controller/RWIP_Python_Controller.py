import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_continuous_are
from scipy.linalg import solve_discrete_are, expm
from scipy.optimize import minimize
import pygame
import sympy as sp
from dataclasses import dataclass



# ==========================================================================
# Parameter containers
# ==========================================================================

@dataclass      # Makes things more automatic, instead of having to create a __init__ function to encompass the variables
class PhysicalParams:
    m_b: float = 1.0    # body mass [kg]
    m_w: float = 1.0    # wheel mass [kg]
    h: float = 0.1      # body side length [m]
    r_w: float = 0.025  # reaction wheel radius [m]
    g: float = 9.82     # gravity [m/s^2]
    
    @property
    def m_tot(self):
        return self.m_b + self.m_w  #Total mass of body and wheel
    
    @property
    def l(self):
        return np.sqrt(2 * self.h**2) / 2   # Length from pivot point to center of body/wheel
    
    @property
    def I_b(self):
        return (2/3) * self.m_b * self.h**2 # Inertia of the body
    
    @property
    def I_w_pivot(self):
        return self.m_w * self.l**2 # Inertia of the wheel around the pivot point
    
    @property
    def I_p(self):
        return self.I_b + self.I_w_pivot    # Inertia around the pivot, total of body and wheel inertia
    
    @property
    def I_w(self):
        return 0.5 * self.m_w * self.r_w**2 #Inertia of the wheel around its own pivot
    
    @property
    def mgl(self):
        return self.m_tot * self.g * self.l # Gravity momentum om the body and wheel



@dataclass
class SimConfig:
    N: int = 10000          # Total number of time steps
    T: float = 5.0         # Length of the simulation
    
    N_mpc: int = 50         # Number of steps ahead the MPC will look
    dt_mpc: float = 0.01   # Mpc time step
    
    
    tau_d: float = 0.01    # Added constant disturbance

    initial_theta_deg: float = np.deg2rad(100.0)   # Initial Error angle
    
    use_torque_limit: bool = True   # Bool to determine wheter a torque limit should be used or not
    u_max: float = 0.5              # Max torque that can be used
    
    use_wheel_speed_limit: bool = True  # Wether a speed limit should apply or not on the wheel
    phi_dot_max_rpm: float = 2000.0     # Max rotational speed of the wheel in RPM
    
    
    # MPC and LQR blending
    theta_bf_min_ml: float = np.deg2rad(5.0)       # This is the lowest angle within the blending function range, below this, its 100% LQR
    theta_bf_max_ml: float = np.deg2rad(8.0)        # This is the highest angle within the blending function range, above this, its 100% MPC
    
    
    # MPC and Swing-up blending
    theta_bf_min_sm: float = np.deg2rad(15.0)
    theta_bf_max_sm: float = np.deg2rad(30.0)
    
    
    # MPC max allowed theta_dot
    theta_dot_limit: float = np.deg2rad(300.0)
    
    
    # Swing-up controller parameters
    k_E: float = 0.01  # Coefficient to determine how much torque the swing up controller should respond with at a certain error.
    kick_fraction: float = 0.5  # If there is no momentum or speed, this is used to give the system a little nudge/kick to start responding, example if the system is in a stable point.
    
    
    @property
    def phi_dot_max_rad(self):
        return self.phi_dot_max_rpm * 2*np.pi / 60  # Max allowable rotational wheel speed in rad/s
    
    @property
    def dt(self):
        return self.T / self.N



# ==========================================================================
# Utility Functions
# ==========================================================================

class ControlFunctionality:
    def wrap_angle(theta):
        """
        Wrap angle to [-pi, pi].
        This keeps theta readable and makes switching logic easier.
        
        FIrst we shift the range from [-180, 180] to [0, 360] for the modulo "%" to work, then we shift it back to [-180, 180] for ease of use
        
        """
        return (theta + np.pi) % (2*np.pi) - np.pi  # Using a wrap angle keeps all the angles within the set limits of pi and -pi. Instead of it continously increasing with rotations to 500pi, it will be kept within one rotation for ease.


    def rad_s_to_rpm(omega):
        return omega * 60 / (2*np.pi)   # Unit conversion between rad/s to RPM


    def clip_torque(u_cmd, cfg):    # Function used to clip the torque to the put torque limits
        u_cmd = float(u_cmd)
        
        if cfg.use_torque_limit:
            return float(np.clip(u_cmd, -cfg.u_max, cfg.u_max))
        
        return u_cmd


    def print_physical_info(p): # Prints out the physical information for the Inertia
        print("I_b =", p.I_b)
        print("I_p =", p.I_p)
        print("I_w =", p.I_w)
        print("mgl =", p.mgl)


    def wheel_speed_constraint(U, state, N, p, dt):
        
        X = np.zeros((N + 1, len(state)))
        X[0] = state
        
        for k in range(N):
            
            X[k+1] = ControlFunctionality.integrate_step(
                X[k],
                U[k],
                p,
                cfg,
                dt
            )
        
        phi_dot = X[1:, 1]

        return np.concatenate([
            cfg.phi_dot_max_rad - phi_dot,
            cfg.phi_dot_max_rad + phi_dot
        ])


    def apply_wheel_speed_limit(u_cmd, state, cfg):
        
        phi_dot = state[1]
        
        limit = cfg.phi_dot_max_rad
        
        # Wheel is too fast in positive direction, dont allow it to accelerate any further
        if phi_dot >= limit and u_cmd > 0:
            u_cmd = 0.0
        
        #  Wheel is too fast in negative direction, dont allow it to accelerate any further
        elif phi_dot <= -limit and u_cmd < 0:
            u_cmd = 0.0
        
        return float(u_cmd)


    def discretize_system(A, B, dt):
        
        n = A.shape[0]
        m = B.shape[1]
        
        M = np.zeros((n + m, n + m))
        
        M[:n, :n] = A
        M[:n, n:] = B
        
        M_d = expm(M * dt)
        
        A_d = M_d[:n, :n]
        B_d = M_d[:n, n:]
        
        return A_d, B_d

    # ==========================================================================
    # Control Design
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
        
        A_d, B_d = ControlFunctionality.discretize_system(A, B, dt)
                
        P = solve_discrete_are(A_d, B_d, Q, R)    # Solved from the Ricatti equation, current cost of the state the controller is in
            
        
        return A_d, B_d, P



    # ==========================================================================
    # Dynamics
    # ==========================================================================

    def nonlinear_dynamics(state, u, p, tau_d=0.0):
        """
        Nonlinear reaction-wheel pendulum dynamics.
        
        State:
            state[0] = phi
            state[1] = phi_dot
            state[2] = theta
            state[3] = theta_dot
            
        """

        phi, phi_dot, theta, theta_dot = state  # All the system states
        
        theta_ddot = (p.mgl * np.sin(theta) - u + tau_d) / p.I_p    # Non-linear dynamics for the error acceleration
        phi_ddot = u / p.I_w - theta_ddot   # Dynamics for the wheel acceleration
        
        return np.array([
            phi_dot,
            phi_ddot,
            theta_dot,
            theta_ddot
        ], dtype=float) # Returns an array of the derivative of the states



    # ==========================================================================
    # Controllers
    # ==========================================================================

    def lqr_controller(state, K):   # LQR controller
        """
        LQR controller.
        
        Uses:
            x_lqr = [theta, theta_dot, phi_dot]
        
        """
        
        phi_dot, theta, theta_dot = state[1], state[2], state[3]  # All current system states
        
        theta = ControlFunctionality.wrap_angle(theta)   # Wraps the error angle within our set range
        
        x_lqr = np.array([
            theta,
            theta_dot,
            phi_dot
        ])  # Puts all the Useable LQR states in a array
        
        u_cmd = -(K @ x_lqr).item() # Calculates the controller input based on the current state
        
        #if u_cmd >= cfg.u_max or u_cmd <= -cfg.u_max:
        #    print(u_cmd)
        u_cmd = ControlFunctionality.apply_wheel_speed_limit(u_cmd, state, cfg)
        
        u_cmd = ControlFunctionality.clip_torque(u_cmd, cfg)
        
        return float(u_cmd) # Returns the controller input


    def mpc_controller(state, U_0, P, p, N, u_prev):   #MPC controller
        """
        
        MPC controller:
            Predicts future outcomes and chooses the most ideal 
        
        """
        
        state[2] = ControlFunctionality.wrap_angle(state[2])
        
        bounds = [(-cfg.u_max, cfg.u_max)]*N
        
        constraints = {
            'type': 'ineq',
            'fun': ControlFunctionality.wheel_speed_constraint,
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
        #print(u_cmd)

        u_cmd = ControlFunctionality.apply_wheel_speed_limit(u_cmd, state, cfg)
        
        u_cmd = ControlFunctionality.clip_torque(u_cmd, cfg)
        
        U_0 = np.concatenate((best.x[1:], [0.0]))
        
        
        return float(u_cmd), U_0 # Returns the controller input and the next starting guess for the next sequence, to save performance.


    def swingup_controller(state, p, cfg):  # Swing-up controller
        """
        Energy-based swing-up controller.
        
        Goal:
            E -> E_des
            
        where:
            E_des = mgl
        
        """

        theta, theta_dot = state[2], state[3]
        
        theta_error = ControlFunctionality.wrap_angle(theta)
    
        E = ControlFunctionality.pendulum_body_energy(theta_error, theta_dot, p)  # Total current pendulum energy
        
        E_des = -p.mgl   # Desired pendilum energy to reach the set target
        E_err = E - E_des   # How much energy is required to be added or removed to reach the desired amount of energy
        
        u_cmd = cfg.k_E * E_err * theta_dot * np.cos(theta) # Swingup controller input based on the K value, Energy error and error rate
        
        # If starting completely still, the energy controller gives zero torque
        # Add a small kick to start the motion.
        #if abs(theta_dot) < 1e-3:
        #    direction = -np.sign(np.sin(theta_error))
            
        #    if direction == 0:
        #        direction = -1.0
                
        #    u_cmd = cfg.kick_fraction * cfg.u_max * direction   # Adds a kick if the pendulum does not have any energy to use.

        # Always apply the limiters
        u_cmd = ControlFunctionality.apply_wheel_speed_limit(u_cmd, state, cfg)
        u_cmd = ControlFunctionality.clip_torque(u_cmd, cfg)
                
        
        return float(u_cmd)



    # ==========================================================================
    # Control Compliments
    # ==========================================================================

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
        
        # Array for normalizing the states to make it easier to implement the cost matrices Q and R
        #NormalizeX = np.array([1, cfg.phi_dot_max_rad, cfg.theta_lqr_enter, cfg.theta_dot_lqr_limit])
        
        for k in range(N):
            
            # Predict next state 
            X[k+1] = ControlFunctionality.integrate_step(X[k], U[k], p, cfg, cfg.dt_mpc)
            
            w_region = 0.0     # Penalty coefficient, we want the mpc to get to the lqr region
            theta_excess = max(0, ControlFunctionality.wrap_angle(X[k+1, 2]) / cfg.theta_bf_min_ml - 1)             # Takes the excess/how far away the current angle is from the ideal angle, within the LQR range.
            theta_dot_excess = 0 #max(0, X[k+1, 3] / cfg.theta_dot_limit - 1)         # Takes the excess/how far away the current angle rate is from the ideal angle rate, within the lqr range.
            
            
            #if(X[k+1, 2] > np.pi):
            #    print(abs(ControlFunctionality.wrap_angle(X[k+1,2])))
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
        
        #cost += e_n_terminal.T @ Q @ e_n_terminal
        
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


    def pendulum_body_energy(theta, theta_dot, p): # Total amount of pendulum energy available
        """
        Body energy relative to upright-angle convention
        
        E = kinetic + potential
        = 1/2 I_p theta_dot^2 + mgl cos(theta)
        
        """
        
        E = 0.5 * p.I_p * theta_dot**2 + p.mgl * (np.cos(theta) + 1)  # Calculates the current energy of the body and wheel based on the current states
        
        
        return E


    def smoothstep_function(theta, bf_min, bf_max):
        
        x_bf = (abs(theta) - bf_min)/(bf_max - bf_min)    # Normalizes the error to within the set range of the blending function
        
        x_bf = np.clip(x_bf, 0, 1)      # Clamps the values within 0-1, as it should not go over or under this
        
        omega = 3*x_bf**2 - 2*x_bf**3   # This is the smooth step function that is used for the blending function
        
        return float(omega)

    #def choose_controller(state, mode, K, U_0, p, cfg, N_mpc, u_mpc, mpc_update):      # MPC only choose controller

        mode = "mpc"

        # Recalculate MPC only when requested
        if mpc_update:
            u_mpc, U_0 = mpc_controller(
                state,
                U_0,
                P_mpc,
                p,
                N_mpc
            )

        u_cmd = u_mpc

        # Apply limits
        u_cmd = apply_wheel_speed_limit(u_cmd, state, cfg)
        u = clip_torque(u_cmd, cfg)

        return U_0, u, mode, u_mpc


    def choose_controller(state, mode, K, U_0, p, cfg, N_mpc, u_mpc, mpc_update, u_prev):  # Deciding which controller is being used where
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
        theta_error = ControlFunctionality.wrap_angle(theta)
        
        # Determines omega depending on the range of the blending function, and normalizes it between 0 and 1
        omega_sm = ControlFunctionality.smoothstep_function(theta_error, cfg.theta_bf_min_sm, cfg.theta_bf_max_sm)
        
        
        # Calls on the smoothstep function to get the value of omega, between 0 and 1, to help determine which controller should be used
        omega_ml = ControlFunctionality.smoothstep_function(theta_error, cfg.theta_bf_min_ml, cfg.theta_bf_max_ml)     
        
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
            
            #if u_cmd >= 0.3 or u_cmd <= 0.3:
            #            print(
            #                f"MPC: {u_mpc}, "
            #                f"Swing: {u_swing}, "
            #                f"omega_sm: {omega_sm}"
            #            )
            
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
            
            #if u_cmd >= 0.3 or u_cmd <= 0.3:
            #    print(
            #        f"MPC: {u_mpc}, "
            #        f"LQR: {u_lqr}, "
            #        f"omega_ml: {omega_ml}"
            #    )
        
        else:
            mode = "lqr"
            
            # LQR Control Input
            u_cmd = ControlFunctionality.lqr_controller(state, K)
                            
                    
        # If the error rate is more than the allowed limit, the mpc or lqr will not take over, and the swing-up controller will continue to be in use
        #if abs(theta_dot) > cfg.theta_dot_limit:
        #    mode = "swing"
        #    u_cmd = ControlFunctionality.swingup_controller(state, p, cfg)
        #    U_0 = np.zeros([N_mpc])
                
        
        # Applies both the wheel speed limit and the torque limit for the motor
        u_cmd = ControlFunctionality.apply_wheel_speed_limit(u_cmd, state, cfg)
        u = ControlFunctionality.clip_torque(u_cmd, cfg) # Clip the input signal between the set torque limit
        
        #if u >= 0.3 or u <= -0.3:
        #    print( u , mode
        #f"theta={np.rad2deg(theta_error):7.2f}°, "
        #f"theta_dot={np.rad2deg(theta_dot):7.2f}°/s, "
        #f"omega_sm={omega_sm:.3f}, "
        #f"omega_ml={omega_ml:.3f}"
        #)
                    
        # returns the initial control guess of the mpc, the current control input, the current mode and the current mpc control input.
        return U_0, u, mode, u_mpc


    # ==========================================================================
    # Integration
    # ==========================================================================

    def integrate_step(state, u, p, cfg, dt):   # Integration step using Semi-Implicit Euler integration
        """
        Semi-implicit Euler integration.
        
        This is usually a little better than plain Euler for mechanical systems
        
        """
        
        phi, phi_dot, theta, theta_dot = state  # All current system states
        
        xdot = ControlFunctionality.nonlinear_dynamics(state, u, p, tau_d=cfg.tau_d) # State derivatives of the nonlinear system dynamics

        phi_ddot = xdot[1]      # Assign the wheel acceleration
        theta_ddot = xdot[3]    # Assign the error acceleration
        
        # Update velocities first
        phi_dot_next = phi_dot + phi_ddot * dt          # Calculates the predicted next wheel speed based on the current wheel angle and wheel acceleration
        theta_dot_next = theta_dot + theta_ddot * dt    # Calculates the predicted next error rate based on the previous and the current error acceleration
        
        # Update positions using new velocities, using Euler integration
        phi_next = phi + phi_dot_next * dt              # Predicts what the next wheel angle will be using the current wheel angle and current wheel speed
        theta_next = theta + theta_dot_next * dt        # Predicts what the next error will be based on the current error and the error rate
        
        theta_next = ControlFunctionality.wrap_angle(theta_next) # Wraps the future predicted error within our set range
        
        return np.array([
            phi_next,
            phi_dot_next,
            theta_next,
            theta_dot_next
        ], dtype=float) # Returns an array of the future predicted states
        
        

    # ==========================================================================
    # Simulation
    # ==========================================================================

    def simulate(initial_theta_deg, p, cfg, K): # Simulation step
        t = np.linspace(0, cfg.T, cfg.N)    # Splits the total amount of time T into a set number of steps N
        dt = cfg.dt    # Discrete time step
        
        X = np.zeros((4, cfg.N))  
        U = np.zeros(cfg.N)
        U_0 = np.zeros([cfg.N_mpc])
        
        mode_history = []
        
        X[2, 0] = initial_theta_deg
        
        # MPC parameters
        mpc_counter = 0
        u_mpc = 0.0
        
        u_prev = 0.0
        
        
        # Start in MPC only if already within its oeprating range
        
        if abs(ControlFunctionality.wrap_angle(X[2, 0])) < cfg.theta_bf_max_ml and abs(ControlFunctionality.wrap_angle(X[2, 0])) > cfg.theta_bf_min_ml: 
            mode = "mpc"    # Change to lqr if you want to use the lqr instead
        
        # Start in LQR only if already within its operating range
        elif abs(ControlFunctionality.wrap_angle(X[2, 0])) < cfg.theta_bf_min_ml:
            mode = "lqr"
        
        # Otherwise start with the swing-up controller
        else:
            mode = "swing"

        # Creates the simulation by running through each time step
        for k in range(cfg.N - 1):
            
            state = X[:, k]
            
            mpc_update = (mpc_counter==0)   # This turns the int into a bool, where mpc_counter == 0, means that mpc_update is True
            
            # Calling omn the choose controller function to decide which controller to run, and sending the current u_mpc command, as well as the mpc_update to decide if its time to recalculate the mpc again
            U_0, u, mode, u_mpc = ControlFunctionality.choose_controller(
                state, 
                mode, 
                K, 
                U_0, 
                p, 
                cfg, 
                cfg.N_mpc, 
                u_mpc, 
                mpc_update,
                u_prev)
            
            # Gives the mpc a new list of starting values, depending on the controller used previously, so it does not start on 0 each time it takes over. using append likes this saves all the numbers starting with the given index, and adds a new number at the end. This is good if you want to move along an array or add new values to an array.
            #U_0 = np.append(U_0[1:], [u])
            
            # Current control input
            U[k] = u
            
            u_prev = u
            
            mode_history.append(mode)   # Stores the history of all the modes/controllers used
            
            # Uses the integrate_step function to estimate the future state
            X[:, k+1] = ControlFunctionality.integrate_step(state, u, p, cfg, cfg.dt)
            
            # Checks wheter 
            if mpc_counter == 0:
                mpc_counter = int(round(cfg.dt_mpc / cfg.dt)) - 1   # Restarts the mpc counter again, removes 1 becuase we start at 0, so we have the correct range inbetween
            else:
                mpc_counter -= 1 # If its not time to recalculate the mpc, then remove one step from the counter, this will continue until its time to recalculate
            
            
        U[-1] = U[-2]
        mode_history.append(mode_history[-1])   # Adds the latest mode in the last mode_history location
        
        return t, X, U, mode_history



    # ==========================================================================
    # Plotting
    # ==========================================================================

    def plot_results(t, X, U, p, cfg):  # Creates plots for the different states and errors.
        phi = X[0, :]       # Wheel angle
        phi_dot = X[1, :]   # Wheel speed
        theta = X[2, :]     # Error
        theta_dot = X[3, :] # Error rate
        
        omega_w = phi_dot + theta_dot   # Absolute wheel speed
        
        fig, ax = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
        
        # Theta
        ax[0].plot(t, np.rad2deg(theta), label="theta [deg]")
        ax[0].axhline(np.rad2deg(cfg.theta_bf_max_sm), linestyle="--", color="r", label="MPC enter")
        ax[0].axhline(-np.rad2deg(cfg.theta_bf_max_sm), linestyle="--", color="r")
        ax[0].axhline(np.rad2deg(cfg.theta_bf_max_ml), linestyle="--", color="g", label="LQR enter")
        ax[0].axhline(-np.rad2deg(cfg.theta_bf_max_ml), linestyle="--", color="g")
        ax[0].set_ylabel("Angle [deg]")
        ax[0].grid()
        ax[0].legend()
        
        # Wheel speeds
        ax[1].plot(t, ControlFunctionality.rad_s_to_rpm(phi_dot), label="relative wheel speed phi_dot [RPM]")
        ax[1].plot(t, ControlFunctionality.rad_s_to_rpm(omega_w), label="absolute wheel speed omega_w [RPM]")
        
        if cfg.use_wheel_speed_limit:
            ax[1].axhline(cfg.phi_dot_max_rpm, linestyle="--", label="wheel speed limit")
            ax[1].axhline(-cfg.phi_dot_max_rpm, linestyle="--")
        
        ax[1].set_ylabel("Speed [RPM]")
        ax[1].grid()
        ax[1].legend()
        
        # Torque
        ax[2].plot(t, U, label="u [Nm]")
        ax[2].axhline(cfg.u_max, linestyle="--", label="torque limit")
        ax[2].axhline(-cfg.u_max, linestyle="--")
        ax[2].set_xlabel("Time [s]")
        ax[2].set_ylabel("Torque [Nm]")
        ax[2].grid()
        ax[2].legend()
        
        # Theta_dot
        ax[3].plot(t, theta_dot, label="Error rate")
        ax[3].axhline(cfg.theta_dot_limit, linestyle="--", color="r", label="LQR Exit")
        ax[3].axhline(-cfg.theta_dot_limit, linestyle="--", color="r", label="LQR Exit")
        ax[3].set_ylabel("Error rate [deg/s]")
        ax[3].grid()
        ax[3].legend()
        
        
        
        
        plt.tight_layout()
        plt.show()



    # ==========================================================================
    # Pygame Visualization
    # ==========================================================================

    def rotate_screen_vector(v, angle):
        """
        Rotate a 2D screen vector by angle.
        
        Screen coordinates:
            x right = positive
            y down = positive
        
        """
        
        c = np.cos(angle)
        s = np.sin(angle)
        
        return np.array([
            c*v[0] - s*v[1],
            s*v[0] + c*v[1]
        ])
        

    def draw_reaction_wheel_system(screen, state, u, mode, p):
        phi, phi_dot, theta, theta_dot = state
        
        width, height = screen.get_size()   # Gets the size of the Pygame window in pixels, both width and height
        
        # Screen setup
        pivot = np.array([width // 2, height // 2 + 180], dtype=float)  # Defines where on the screen that the pivot is drawn
        
        # Drawing scale
        pixels_per_meter = 1800                                     # How many pixels should go for each meter in the simulation
        body_side_px = p.h * pixels_per_meter                       # How many pixels one side of the body should be
        wheel_radius_px = max(18, int(p.r_w * pixels_per_meter))    # How many pixels the wheel_radius is in length
        
        # Direction from pivot to box center.
        # theta = 0 means center is directly above pivot
        center_dir = np.array([
            np.sin(theta),
            -np.cos(theta)
        ])
        
        # A square corner-to-center diagonal is 45 degrees from each side.
        # So the two box edges from the pivot are +/- 45 degrees around center_dir.
        edge_1_dir = ControlFunctionality.rotate_screen_vector(center_dir, np.pi / 4)
        edge_2_dir = ControlFunctionality.rotate_screen_vector(center_dir, -np.pi / 4)
        
        # Four corners of the square body
        corner_0 = pivot                                                # Pivot corner, the axle the body rotates around
        corner_1 = pivot + body_side_px * edge_1_dir                    # Corners are based on a upright stable position, making the corner be based on the hypothenus
        corner_2 = pivot + body_side_px * (edge_1_dir + edge_2_dir)     # Corner is the top corner of the body, furthest away from the pivot point, it is calculated using the length of both the sides to calculate the point of the top corner.
        corner_3 = pivot + body_side_px * edge_2_dir                    # Corner is the right corner going to the right at 45 degrees.
        
        # Creates a list of the corners and stores them as integers instead of floats.  
        body_corners = [
            corner_0.astype(int),
            corner_1.astype(int),
            corner_2.astype(int),
            corner_3.astype(int)
        ]
        
        # Body center, here we draw the reaction wheel
        wheel_center = 0.5 * (corner_0 + corner_2)
        
        
        # Colors
        background = (20, 20, 25)       # Background color
        body_fill = (45, 50, 60)        # Body fill color
        body_outline = (230, 230, 230)  # Body outline color
        wheel_color = (80, 160, 255)    # Wheel color
        spoke_color = (255, 220, 120)   # Spoke color
        pivot_color = (255, 120, 120)   # Pivot point color
        center_color = (120, 255, 150)  # Center point color
        text_color = (240, 240, 240)    # Text color
        
        screen.fill(background)         # Sets the screen color to the background color
        
        # Draw upright reference line
        reference_length = p.l * pixels_per_meter
        ref_top = pivot + np.array([0, -reference_length])
        pygame.draw.line(
            screen,
            (80, 80, 80),
            pivot.astype(int),
            ref_top.astype(int),
            2
        )
        
        # Draw filled rotating body
        pygame.draw.polygon(
            screen,
            body_fill,
            body_corners
        )
        
        # Draw body outline
        pygame.draw.polygon(
            screen,
            body_outline,
            body_corners,
            width=4
        )
        
        # Draw pivot point
        pygame.draw.circle(
            screen,
            pivot_color,
            pivot.astype(int),
            8
        )
        
        # Draw center of mass / wheel center marker
        pygame.draw.circle(
            screen,
            center_color,
            wheel_center.astype(int),
            5
        )
        
        # Draw reaction wheel
        pygame.draw.circle(
            screen,
            wheel_color,
            wheel_center.astype(int),
            wheel_radius_px,
            width=4
        )
        
        # Absolute wheel angle = body angle + relative wheel angle
        wheel_abs_angle = theta + phi
        
        spoke_end = wheel_center + np.array([
            wheel_radius_px * np.sin(wheel_abs_angle),
            -wheel_radius_px * np.cos(wheel_abs_angle)
        ])
        
        # Draw wheel spoke
        pygame.draw.line(
            screen,
            spoke_color,
            wheel_center.astype(int),
            spoke_end.astype(int),
            4
        )
        
        # Text overlay
        font = pygame.font.SysFont("consolas", 20)
        
        lines = [
            f"mode: {mode}",
            f"theta: {np.rad2deg(theta): .2f} deg",
            f"theta_dot: {np.rad2deg(theta_dot): .2f} deg/s",
            f"phi_dot: {phi_dot * 60 / (2*np.pi): .1f} RPM",
            f"u: {u: .4f} Nm",
        ]
        
        y = 20
        for line in lines:
            text = font.render(line, True, text_color)
            screen.blit(text, (20, y))
            y += 26
        
        
    def run_pygame_simulation(p, cfg, K, initial_theta_deg):
        pygame.init()
        
        screen = pygame.display.set_mode((900, 700))
        pygame.display.set_caption("Reaction Wheel Inverted Pendulum")
        
        clock = pygame.time.Clock()
        
        # Initial state:
        # [phi, phi_dot, theta, theta_dot]
        state = np.zeros(4, dtype=float)
        state[2] = initial_theta_deg
        # Start in MPC only if already within its oeprating range
            
        if initial_theta_deg < cfg.theta_bf_max_ml and initial_theta_deg > cfg.theta_bf_min_ml: 
            mode = "mpc"    # Change to lqr if you want to use the lqr instead
            
        # Start in LQR only if already within its operating range
        elif initial_theta_deg < cfg.theta_bf_min_ml:
            mode = "lqr"
            
        # Otherwise start with the swing-up controller
        else:
            mode = "swing"
        
        physics_dt = cfg.dt
        accumulator = 0.0
        
        running = True
        u = 0.0
        u_prev = 0.0
        
        
        # MPC parameters
        mpc_counter = 0
        u_mpc = 0.0
        
        U_0 = np.zeros([cfg.N_mpc])
        
        while running:
            frame_dt = clock.tick(60) / 1000.0
            accumulator += frame_dt
            
            mpc_update = (mpc_counter==0)   # This turns the int into a bool, where mpc_counter == 0, means that mpc_update is True
                    
            # -------------------------
            # Events / keyboard input
            # -------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        state = np.zeros(4, dtype=float)
                        state[2] = np.deg2rad(initial_theta_deg)
                        mode = "swing"
                    
                    if event.key == pygame.K_SPACE:
                        # Give the body a small angular velocity kick
                        state[3] += np.deg2rad(50)
            # -------------------------
            # Physics update
            # -------------------------
            
            
            while accumulator >= physics_dt:
                
                U_0, u, mode, u_mpc = ControlFunctionality.choose_controller(
                    state, 
                    mode, 
                    K, 
                    U_0, 
                    p, 
                    cfg, 
                    cfg.N_mpc, 
                    u_mpc, 
                    mpc_update,
                    u_prev
                    )
                
                state = ControlFunctionality.integrate_step(
                    state,
                    u,
                    p,
                    cfg,
                    physics_dt
                )
                
                u_prev = u
                accumulator -= physics_dt
                
                # Checks wheter 
                if mpc_counter == 0:
                    mpc_counter = int(round(cfg.dt_mpc / cfg.dt)) - 1   # Restarts the mpc counter again, removes 1 becuase we start at 0, so we have the correct range inbetween
                else:
                    mpc_counter -= 1 # If its not time to recalculate the mpc, then remove one step from the counter, this will continue until its time to recalculate
                        
            
            # -------------------------
            # Draw
            # -------------------------
            ControlFunctionality.draw_reaction_wheel_system(screen, state, u, mode, p)
            pygame.display.flip()
        
        pygame.quit()



# ==========================================================================
# Main script
# ==========================================================================

p = PhysicalParams()    # Physical parameters
cfg = SimConfig()   # System configuration for the start of the simulation

#print_physical_info(p)  # Printing the physical information

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

R_mpc = np.array([[10e4]])

R_delta_u_mpc = 1000.0

A_LQR, B_LQR, K, P_lqr = ControlFunctionality.build_lqr_controller(p, Q_lqr, R_lqr)

A_MPC, B_MPC, P_mpc = ControlFunctionality.build_mpc_controller(p, Q_mpc, R_mpc, cfg.dt_mpc)

print("K =", K)

t, X, U, mode_history = ControlFunctionality.simulate(cfg.initial_theta_deg, p, cfg, K)

#print(mode_history)
ControlFunctionality.plot_results(t, X, U, p, cfg)

ControlFunctionality.run_pygame_simulation(p, cfg, K, cfg.initial_theta_deg)