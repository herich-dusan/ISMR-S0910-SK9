#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

from autonomous_bicycle.map import Map
from autonomous_bicycle.dijsktra import Dijkstra

from functools import partial

class MyNode(Node):
    def __init__(self):
        super().__init__("the_node"); # the name shown when executed 
        # self.create_timer(1.0, self.timer_callback);

        self.map = Map(10);
        self.nodes = self.map.get_nodes();

    def send_request(self):
        while True:
            a = int(input(f"Enter bicycle row [0, {self.map.size - 1}]: "))
            b = int(input(f"Enter bicycle column [0, {self.map.size - 1}]: "))
            self.call_find_path_service(a, b)
            if input("Do you want to continue? (y/n): ").lower() == 'n':
                break

    def call_find_path_service(self, a, b):
        client = self.create_client(AddTwoInts, "/add_two_ints");
        
        while not(client.wait_for_service(1.0)):
            self.get_logger().warn("Service is not up!");

        request = AddTwoInts.Request();
        request.a = a;
        request.b = b;

        future = client.call_async(request); # send
        future.add_done_callback(partial(self.callback_find_path_service, a=request.a, b=request.b));  

    def callback_find_path_service(self, future, a, b):
        try:
            response = future.result();

            start = self.nodes[self.map.size*a + b];
            end = self.nodes[-1];

            Wybe = Dijkstra(self.map, start, end);
            Wybe.find_path();
            path = Wybe.get_path();
            ans = 0;

            for i, node in enumerate(path[:-1]):
                ans += node.get_distance(path[i + 1]);
            
            self.get_logger().info(f"{ans}");
            print(f"{ans}\n");
            return None;
        
        except Exception:
            self.get_logger().error("Call failed %r" % (Exception,));


def main(args=None):
    rclpy.init(args=args);

    node = MyNode();

    node.send_request();
    rclpy.spin(node);

    rclpy.shutdown();


if __name__ == "__main__":
    main();