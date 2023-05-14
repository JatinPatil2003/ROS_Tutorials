#!/usr/bin/env python3
import rospy
import math
from sensor_msgs.msg import JointState

def control_joints(arm1, arm2):
    joint_state = JointState()
    joint_state.header.stamp = rospy.Time.now()
    joint_state.name = ['joint1', 'joint2']

    arm1_radian = math.radians(arm1)
    arm2_radian = math.radians(arm2)

    joint_state.position = [arm1_radian, arm2_radian]

    joint_publisher.publish(joint_state)
    rate.sleep()

rospy.init_node('joint_control_node', anonymous=True)
joint_publisher = rospy.Publisher('/joint_states', JointState, queue_size=10)
rate = rospy.Rate(50)

while not rospy.is_shutdown():
    # arm1 = float(input("Enter angle of arm1 [-60 : 60] : "))
    # arm2 = float(input("Enter angle of arm2 [-60 : 60] : "))
    arm1 = 30
    arm2 = 45
    
    control_joints(arm1, arm2)