#!/usr/bin/env python3

from std_msgs.msg import Int16
import rospy

class NumberKEngine(object):
    def __init__(self):
        self.setup_ros()
        self.loop()


    def setup_ros(self):
        """
        Initializes the node 'nodeA' and the publisher.
        """
        rospy.init_node('nodeA')
        self.pub = rospy.Publisher('/engstrom', Int16, queue_size=1)

    def loop(self):
        """
        This loop increments the value of k by n=4 with a frequency
        of 20 Hz, as specified in the problem spcecification. 
        
        The value of k is then published to the topic '/engstrom' as
        a message of the type std_msgs Int16. 

        As there is an upper limit to what value can be stored in the
        data type std_msgs Int16, I decided to reset the value of k 
        to 1 once every time k reaches beyond 1000.  
        """
        rate = rospy.Rate(20)
        self.k = 1
        self.n = 4

        while not rospy.is_shutdown():
            self.k += self.n
            if self.k >= 1000:
                self.k = 1

            self.pub.publish(self.k)
            rate.sleep()

if __name__ == '__main__':
    NumberKEngine()