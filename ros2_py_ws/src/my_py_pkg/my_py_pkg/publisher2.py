#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HellowWorldPublisher(Node):
    def __init__(self):
        super().__init__('hello_world_pub')
        self.pub = self.create_publisher(String, "hello_world", 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        msg = String()
        msg.data = "Hello World" + str(self.counter)
        self.pub.publish(msg)
        self.counter += 1
       

def main(args=None):
    rclpy.init()
    my_pub = HellowWorldPublisher()
    print("Publisher has been started...")

    try:
        rclpy.spin(my_pub)
    except KeyboardInterrupt:
        print("Shutting down publisher node...")
        my_pub.destroy_node()

if __name__ == '__main__':
    main()