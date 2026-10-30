import pygame
import numpy as np
import matplotlib.pyplot as plt
import ros2_ws.src.rwip_ros2_package.msg as ControlInput    


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
        self.u_max = 1.0                        # Maximum torque in Nm
        
        # MPC parameters
        self.dt_mpc = 0.1                       # MPC update interval in seconds
        self.N_mpc = 20                         # Number of MPC steps
        
        # Controller switching thresholds
        self.theta_bf_max_sm = np.deg2rad(10)   # Threshold for switching to MPC (small)
        self.theta_bf_max_ml = np.deg2rad(20)   # Threshold for switching to LQR (medium)
        self.theta_bf_min_ml = np.deg2rad(5)    # Threshold for switching to LQR (minimum)
        
        # LQR exit threshold
        self.theta_dot_limit = np.deg2rad(30)   # Threshold for exiting LQR control

def rad_s_to_rpm(omega):
    return omega * 60 / (2 * np.pi) # Converts angular velocity from radians per second to revolutions per minute (RPM)

def wrap_angle(theta):
        """
        Wrap angle to [-pi, pi].
        This keeps theta readable and makes switching logic easier.
        
        FIrst we shift the range from [-180, 180] to [0, 360] for the modulo "%" to work, then we shift it back to [-180, 180] for ease of use
        
        """
        return (theta + np.pi) % (2*np.pi) - np.pi  # Using a wrap angle keeps all the angles within the set limits of pi and -pi. Instead of it continously increasing with rotations to 500pi, it will be kept within one rotation for ease.

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
        
        if abs(wrap_angle(X[2, 0])) < cfg.theta_bf_max_ml and abs(wrap_angle(X[2, 0])) > cfg.theta_bf_min_ml: 
            mode = "mpc"    # Change to lqr if you want to use the lqr instead
        
        # Start in LQR only if already within its operating range
        elif abs(wrap_angle(X[2, 0])) < cfg.theta_bf_min_ml:
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
        u_node = U[-1]
        mode_history.append(mode_history[-1])   # Adds the latest mode in the last mode_history location
        
        return t, X, U, mode_history


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
        ax[1].plot(t, rad_s_to_rpm(phi_dot), label="relative wheel speed phi_dot [RPM]")
        ax[1].plot(t, rad_s_to_rpm(omega_w), label="absolute wheel speed omega_w [RPM]")
        
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
        edge_1_dir = rotate_screen_vector(center_dir, np.pi / 4)
        edge_2_dir = rotate_screen_vector(center_dir, -np.pi / 4)
        
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
            draw_reaction_wheel_system(screen, state, u, mode, p)
            pygame.display.flip()
        
        pygame.quit()


cfg = SimConfig()

