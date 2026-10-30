#!/usr/bin/env python3
import sys
import numpy as np

sys.path.append(
    '/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/Python/controller_package'
)

import rclpy    # Import the ROS2 Python client library
from rclpy.node import Node     # Import the Node class from rclpy.node module
from rwip_ros2_package.msg import ControlInput  # Imports the ControlInput message
from rwip_ros2_package.msg import States        # Imports the States message
import adcs_controller.RWIP_Python_Controller   # Imports the controller script functionality



# Class for the controller node
class ControllerNode(Node):

    # Initialization of the controller node
    def __init__(self):

        # Call the constructor of the parent class (Node) with the name 'controller_node'
        super().__init__('controller_node')

        #controller = adcs_controller.RWIP_Python_Controller()  # Create an instance of the ControlFunctionality class 

        # Create a publisher for the 'controller' topic with message type 'ControlInput' and a queue size of 10
        #self.publisher = self.create_publisher(ControlInput, 'control_input', 10)
        #self.subscription = self.create_subscription(States, 'states', 10)  # Create a subscription to the 'states' topic with message type 'States' and a callback function

        self.timer = self.create_timer(1.0, self.publish_control)
        self.timer = self.create_timer(1.0, self.subscribe_states)

        #msg = ControlInput()  # Create an instance of the ControlInput message
        #msg.motor_torque = adcs_controller.RWIP_Python_Controller.U[-1]  # Set the motor torque value in the message

        # Create a publisher for the 'controller' topic with message type 'Controller' and a queue size of 10
        self.get_logger().info('Controller node started!')

    def publish_control(self):
        msg = ControlInput()
        msg.motor_torque = adcs_controller.RWIP_Python_Controller.U[-1]  # Get the latest control input from the controller
        self.get_logger().info('Control Input Published: motor_torque=%.2f' % msg.motor_torque)

    def subscribe_states(self):
        # Create a subscription to the 'states' topic with message type 'States' and a callback function
        msg = States()
        states = np.array([msg.phi, msg.phi_dot, msg.theta, msg.theta_dot])  # Create a numpy array from the received states
        states = adcs_controller.RWIP_Python_Controller.X[-1]   
        self.get_logger().info('States Received: phi=%.2f, phi_dot=%.2f, theta=%.2f, theta_dot=%.2f' % (states[0], states[1], states[2], states[3]))
        
        



# Main function to run the controller node
def main(args=None):

    # Initialize the ROS2 Python client library
    rclpy.init(args=args)

    

    # Create an instance of the ControllerNode class
    node = ControllerNode()

    # Keep the node running and processing callbacks until it is shut down
    rclpy.spin(node)

    # Destroy the node and shut down the ROS2 client library when done
    node.destroy_node()

    # Shutdown the ROS2 Python client library
    rclpy.shutdown()

# Entry point for the script
if __name__ == '__main__':

    # Call the main function to start the controller node
    main()
