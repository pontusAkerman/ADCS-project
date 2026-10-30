import numpy as np
import ros2_ws.src.rwip_ros2_package.msg as ControlInput 
import ros2_ws.src.rwip_ros2_package.msg as States
import utility as util
from RWIP_Simconfig import SimConfig as cfg

# Class containing the dynamics of the reaction-wheel inverted pendulum system, including the nonlinear dynamics and the linearized dynamics for control design.
class Dynamics():
    
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