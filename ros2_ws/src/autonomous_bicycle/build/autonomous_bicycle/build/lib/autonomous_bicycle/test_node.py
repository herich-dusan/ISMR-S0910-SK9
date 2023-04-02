#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    

    def __init__(self):
        self.__time = 0;
        super().__init__("the_node"); # the name shown when executed 
        self.create_timer(1.0, self.timer_callback);
        
    def timer_callback(self):
        self.get_logger().info("Shalom {}" .format(self.__time));
        self.__time += 1;


def main(args=None):
    rclpy.init(args=args);

    node = MyNode();

    rclpy.spin(node); # inf
    rclpy.shutdown(); # kill


if __name__ == "__main__":
    main();