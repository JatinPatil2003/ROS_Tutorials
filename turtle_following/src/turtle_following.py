#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

x = 0
y = 0
yaw = 0

def posecallback(pose_msg):
    global x
    global y
    global yaw
    x = pose_msg.x
    y = pose_msg.y
    ang = 0
    if(pose_msg.theta < 0):
        ang = 6.28 - pose_msg.theta
    yaw = pose_msg.theta
#     print(x," ", y, " ", yaw)



def go_to_goal(x_goal, y_goal):
    global x
    global y, yaw

    velocity_message = Twist()
    cmd_vel_topic='/turtle1/cmd_vel'

    while (True):
        current_pose = rospy.wait_for_message('/turtle2/pose', Pose)
        xi = current_pose.x
        yi = current_pose.y
        yawi = current_pose.theta
        K_linear = 0.5 
        distance = abs(math.sqrt(((x_goal-xi) ** 2) + ((y_goal-yi) ** 2)))

        linear_speed = distance * K_linear


        K_angular = 4.0
        desired_angle_goal = math.atan2(y_goal-yi, x_goal-xi)
        angular_speed = (desired_angle_goal-yawi)*K_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_pub.publish(velocity_message)
        
        #print velocity_message.linear.x
        #print velocity_message.angular.z
#         print 'x=', x, 'y=',y


        if (distance <0.01):
            break


rospy.init_node('turtlesim_following', anonymous=True)
pose_sub = rospy.Subscriber('/turtle1/pose', Pose, posecallback)
velocity_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    x_goal = x
    y_goal = y
    velocity_message = Twist()
    current_pose = rospy.wait_for_message('/turtle2/pose', Pose)
    xi = current_pose.x
    yi = current_pose.y
    yawi = current_pose.theta
    K_linear = 0.7
    distance = abs(math.sqrt(((x_goal-xi) ** 2) + ((y_goal-yi) ** 2)))

    linear_speed = distance * K_linear


    K_angular = 4.0
    desired_angle_goal = math.atan2(y_goal-yi, x_goal-xi)
    angular_speed = (desired_angle_goal-yawi)*K_angular

    velocity_message.linear.x = linear_speed
    velocity_message.angular.z = angular_speed

    velocity_pub.publish(velocity_message)
'''
while not rospy.is_shutdown():
    current_pose = rospy.wait_for_message('/turtle2/pose', Pose)
    diff_x = x - current_pose.x
    diff_y = y - current_pose.y
    t2ang = current_pose.theta
#     t2ang = 0
#     if(current_pose.theta < 0):
#         t2ang = 6.28 - current_pose.theta
#     else:
#         t2ang = current_pose.theta
    distance = abs(pow((pow(diff_x,2)+pow(diff_y,2)), 0.5))
#     if(t2ang < 0):
#         angle = math.atan2(diff_y, diff_x) - t2ang
#     else:
    angle = math.atan2(diff_y, diff_x) - t2ang
#     angle = current_pose.theta - yaw
#     if(t1ang >= 0.0 and t2ang >= 0.0):
#         angle = t1ang - t2ang
#     elif(t1ang < 0.0 and t2ang < 0.0):
#         angle = t2ang - t1ang
#     else:
#         angle = t1ang + t2ang
    #print(current_pose.x," ", current_pose.y, " ", current_pose.theta)
    
    if(distance > 0.1 ):
        twist_msg = Twist()
        twist_msg.linear.x = 1 * distance
        twist_msg.angular.z = 1 * angle
        velocity_pub.publish(twist_msg)
        print(distance,angle,t2ang)
    else:
        twist_msg = Twist()
        twist_msg.linear.x = 0
        twist_msg.angular.z = 0
        velocity_pub.publish(twist_msg)
        print("Distance is ", distance)
    rate.sleep()

'''
'''
while not rospy.is_shutdown():
	current_pose = rospy.wait_for_message('/turtle2/pose', Pose)
	go_to_goal(x,y,current_pose)
	
	'''
