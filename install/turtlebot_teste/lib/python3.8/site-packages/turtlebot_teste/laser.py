import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class LaserSub(Node):
    def __init__(self):
        # Cria subscriber para scan
        super().__init__('lasersub')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.listener_callback,
            rclpy.qos.qos_profile_sensor_data
        )
        self.subscription

    def listener_callback(self, msg):
        self.norte = msg.ranges[0]
        self.noroeste = msg.ranges[45]
        self.oeste = msg.ranges[90]
        self.sul = msg.ranges[180]
        self.leste = msg.ranges[270]
        self.nordeste = msg.ranges[315]

def main(args=None):
    rclpy.init(args=args)
    laser = LaserSub()
    while(True):
        rclpy.spin_once(laser)
        print("Distância do leste: " + str(laser.leste))


if __name__ == '__main__':
    main()