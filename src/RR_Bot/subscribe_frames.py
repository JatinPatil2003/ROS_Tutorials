#!/usr/bin/env python3

import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('arm1_arm2_listener_node')

    listener = tf.TransformListener()
    rate = rospy.Rate(50.0)
    listener.waitForTransform('/arm1', '/arm2', rospy.Time(), rospy.Duration(1.0))
    
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/arm1', '/arm2', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        quaternion = rot
        rpy=tf.transformations.euler_from_quaternion(quaternion)
        print('Translation: ','(',trans[0],',',trans[1],',',trans[2],')',' rpy: ','(',rpy[0],',',rpy[1],',',rpy[2],')')


        rate.sleep()