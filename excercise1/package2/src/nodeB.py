#!/usr/bin/env python3

# Subscriber recieving "engstrom" message from nodeA.
# divide received number by q = 0.15 and publish result 
# with 20 Hz to topic /kthfs/result
# make py files executable with $ chmod +x filename.py

from std_msgs.msg import Int16, Float64
import rospy

class ResultProducer(object):
    def __init__(self):
        self.k = Int16(1)
        self.setup_ros()

        self.loop()
        

    def setup_ros(self):
        """
        Build the node, subscriber and publisher
        """
        rospy.init_node('nodeB')
        rospy.Subscriber('/engstrom', Int16, self.k_callback , queue_size=1)
        self.pub = rospy.Publisher('/kthfs/result', Float64, queue_size=1)

    def k_callback(self, msg):
        self.k = msg

    def loop(self):
        rate = rospy.Rate(20)
        self.q = 0.15

        while not rospy.is_shutdown():
            result = self.k.data / self.q 
            self.pub.publish(result)
            rate.sleep()

if __name__ == '__main__':
    ResultProducer()
