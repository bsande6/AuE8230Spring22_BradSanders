#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

class SquareClosedLoop():
    def __init__(self):
        rospy.init_node('square_closedloop', anonymous=True)

        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist, queue_size=10)

        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)
        self.odom_pose = None

    def __odom_ros_sub(self, msg):
        self.odom_pose = msg.pose.pose

    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):

        return math.sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def stop_moving(self, vel_msg):
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        self.velocity_publisher.publish(vel_msg)

    def move(self):
        vel_msg = Twist()
        goal_pose = Pose()
        while not rospy.is_shutdown():
            goal_pose.x = 8
            goal_pose.y = 5
            while self.euclidean_distance(goal_pose) > .01 and not self.pose.x > 8:
                vel_msg.linear.x = 0.2
                self.velocity_publisher.publish(vel_msg)
            self.stop_moving(vel_msg)

            goal_pose.x = 8
            goal_pose.y = 8
            while self.euclidean_distance(goal_pose) > .01 and not self.pose.y > 8:
                vel_msg.linear.y = 0.2
                self.velocity_publisher.publish(vel_msg)
            self.stop_moving(vel_msg)

            goal_pose.x = 5
            goal_pose.y = 8
            while self.euclidean_distance(goal_pose) > .01 and not self.pose.x < 5:
                vel_msg.linear.x = -0.2
                self.velocity_publisher.publish(vel_msg)
            self.stop_moving(vel_msg)

            goal_pose.x = 5
            goal_pose.y = 5
            while self.euclidean_distance(goal_pose) > .01 and not self.pose.y < 5:
                vel_msg.linear.y = -0.2
                self.velocity_publisher.publish(vel_msg)
            self.stop_moving(vel_msg)
        
        self.stop_moving(vel_msg)
        
if __name__ == '__main__':
    try:
        square = SquareClosedLoop()
        square.move()
    except rospy.ROSInterruptException: pass

