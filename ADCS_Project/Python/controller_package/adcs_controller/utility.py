import numpy as np
from scipy.linalg import solve_continuous_are
from scipy.linalg import solve_discrete_are, expm
from scipy.optimize import minimize


# ==========================================================================
# Utility Functions
# ==========================================================================

def clip_torque(u_cmd, use_torque_limit, u_max):    # Function used to clip the torque to the put torque limits
    u_cmd = float(u_cmd)
        
    if use_torque_limit:
        return float(np.clip(u_cmd, -u_max, u_max))
        
    return u_cmd

def rad_s_to_rpm(omega):
    return omega * 60 / (2 * np.pi) # Converts angular velocity from radians per second to revolutions per minute (RPM)

def wrap_angle(theta):
        """
        Wrap angle to [-pi, pi].
        This keeps theta readable and makes switching logic easier.
        
        FIrst we shift the range from [-180, 180] to [0, 360] for the modulo "%" to work, then we shift it back to [-180, 180] for ease of use
        
        """
        return (theta + np.pi) % (2*np.pi) - np.pi  # Using a wrap angle keeps all the angles within the set limits of pi and -pi. Instead of it continously increasing with rotations to 500pi, it will be kept within one rotation for ease.

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


def smoothstep_function(theta, bf_min, bf_max):
        
    x_bf = (abs(theta) - bf_min)/(bf_max - bf_min)    # Normalizes the error to within the set range of the blending function
        
    x_bf = np.clip(x_bf, 0, 1)      # Clamps the values within 0-1, as it should not go over or under this
        
    omega = 3*x_bf**2 - 2*x_bf**3   # This is the smooth step function that is used for the blending function
        
    return float(omega)


def apply_wheel_speed_limit(u_cmd, state, wheel_speed_limit):
        
        phi_dot = state[1]
        
        limit = wheel_speed_limit
        
        # Wheel is too fast in positive direction, dont allow it to accelerate any further
        if phi_dot >= limit and u_cmd > 0:
            u_cmd = 0.0
        
        #  Wheel is too fast in negative direction, dont allow it to accelerate any further
        elif phi_dot <= -limit and u_cmd < 0:
            u_cmd = 0.0
        
        return float(u_cmd)

