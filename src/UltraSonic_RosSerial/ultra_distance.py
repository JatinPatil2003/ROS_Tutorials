#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Range

def get_Distance(msg):
    distance = msg.range
    #rospy.loginfo("Distance : %f",distance)
    print("Distance : ",distance)

rospy.init_node('ultrasound_subscriber', anonymous=True)
rospy.Subscriber("/ultrasound", Range, get_Distance)
rospy.spin()




