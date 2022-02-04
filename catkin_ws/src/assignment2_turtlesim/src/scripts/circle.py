#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def circle():
    # Starts a new node
    rospy.init_node('circle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    r = rospy.Rate(10)

    vel_msg.linear.x = 0.5
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0.5

    while not rospy.is_shutdown():
        print(vel_msg)
        velocity_publisher.publish(vel_msg)
        r.sleep()

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException: pass