#!/usr/bin/env python3      # Linux Instruction to use Python3 interpreter

import rclpy    # Import the ROS2 Python client library
from rclpy.node import Node     # Import the Node class from rclpy.node module


# Class for the controller node
class ControllerNode(Node):

    # Initialization of the controller node
    def __init__(self):

        # Call the constructor of the parent class (Node) with the name 'controller_node'
        super().__init__('controller_node')

        # Create a publisher for the 'controller' topic with message type 'Controller' and a queue size of 10
        self.get_logger().info('Controller node started!')


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
