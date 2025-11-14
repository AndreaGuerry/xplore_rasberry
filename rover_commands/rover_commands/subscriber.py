import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import serial.tools.list_ports

class TrajectorySubscriber(Node):
    def __init__(self):
        self.ser=serial.Serial("/dev/ttyUSB0", 115200)
        super().__init__('Info_subscriber')
        # TODO: Create a subscriber of type Twist, that calls listener_callback
        # Your code here
        self.subscriber_ = self.create_subscription(String,'command', self.listener_callback,18)
        self.get_logger().info('Subscriber node has been started.')


    def listener_callback(self, msg):
        # TODO: Interpret the received commands and log the result using self.get_logger().info()
        # Your code here
        self.get_logger().info('I recieved: ' + msg.data)
        self.ser.write(str.encode(msg.data))

        
def main(args=None):
    rclpy.init(args=args)
    node = TrajectorySubscriber()
    printable=list(serial.tools.list_ports.comports())
    for p in printable:
        print (p)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
