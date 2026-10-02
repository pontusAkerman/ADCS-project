#!/usr/bin/env python3
import sys

sys.path.append(
    '/home/pontus-akerman/Desktop/ADCS-project/ADCS_Project/Python/controller_package'
)

import rclpy    # Import the ROS2 Python client library
from rclpy.node import Node     # Import the Node class from rclpy.node module
from rwip_ros2_package.msg import ControlInput
from adcs_controller.RWIP_Python_Controller import ControlFunctionality



# Class for the controller node
class ControllerNode(Node):

    # Initialization of the controller node
    def __init__(self):

        # Call the constructor of the parent class (Node) with the name 'controller_node'
        super().__init__('controller_node')

        controller = ControlFunctionality()  # Create an instance of the ControlFunctionality class 

        # Create a publisher for the 'controller' topic with message type 'ControlInput' and a queue size of 10
        self.publisher = self.create_publisher(ControlInput, 'control_input', 10)

        self.timer = self.create_timer(1.0, self.publish_control)

        msg = ControlInput()  # Create an instance of the ControlInput message
        msg.motor_torque = 0.0  # Set the motor torque value in the message

        # Create a publisher for the 'controller' topic with message type 'Controller' and a queue size of 10
        self.get_logger().info('Controller node started!')

    def publish_control(self):
        msg = ControlInput()
        msg.motor_torque = 0.0
        self.get_logger().info('Control Input Published: motor_torque=%.2f' % msg.motor_torque)
        self.publisher.publish(msg)



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
