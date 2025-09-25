#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HellowWorldSubscriber(Node):
    def __init__(self):
        super().__init__('hello_world_sub')
        self.sub = self.create_subscription(String, "hello_world", self.sub_callback, 10)

    def sub_callback(self, msg):
        self.get_logger().info("I heard: " + msg.data)

def main(args=None):
    rclpy.init()
    my_sub = HellowWorldSubscriber()
    print("Waiting for the publisher data...")

    try:
        rclpy.spin(my_sub)
    except KeyboardInterrupt:
        print("Shutting down Subscriber node...")
        my_sub.destroy_node()

if __name__ == '__main__':
    main()