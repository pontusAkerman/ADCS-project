import numpy as np

class SimConfig():
    def __init__(self):
        self.initial_theta_deg = 0.0  # Initial angle of the pendulum in degrees
        self.T = 10.0                  # Total simulation time in seconds
        self.N = 1000                  # Number of simulation steps
        self.dt = self.T / self.N      # Time step size
        
        # Wheel speed limit
        self.use_wheel_speed_limit = True       # Flag to enable/disable wheel speed limit
        self.phi_dot_max_rpm = 100.0            # Maximum wheel speed in RPM
        
        # Torque limit
        self.use_torque_limit = True            # Flag to enable/disable torque limit
        self.u_max = 1.0                        # Maximum torque in Nm

        # Control Parameters
        self.tau_d = 0.01

        # MPC parameters
        self.dt_mpc = 0.1                       # MPC update interval in seconds
        self.N_mpc = 20                         # Number of MPC steps
        
        # Controller switching thresholds
        self.theta_bf_max_sm = np.deg2rad(30.0)   # Threshold for switching to MPC (small)
        self.theta_bf_min_sm = np.deg2rad(15.0)   # Threshold for switching to MPC (minimum)
        self.theta_bf_max_ml = np.deg2rad(8.0)   # Threshold for switching to LQR (medium)
        self.theta_bf_min_ml = np.deg2rad(5.0)    # Threshold for switching to LQR (minimum)
        
        # LQR exit threshold
        self.theta_dot_limit = np.deg2rad(300.0)   # Threshold for exiting LQR control

    
    def phi_dot_max_rad(self):
        return self.phi_dot_max_rpm * 2*np.pi / 60  # Max allowable rotational wheel speed in rad/s
        
        
    def dt(self):
        return self.T / self.N

