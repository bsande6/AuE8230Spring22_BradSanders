#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def square_openloop():
    # Starts a new node
    rospy.init_node('square_openloop', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    def move_forward(distance, vel_msg):
        vel_msg.linear.x = 0.2
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        speed = vel_msg.linear.x
        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
            
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

    def turn_left(angle, vel_msg):
        vel_msg.linear.x = 0.
        vel_msg.angular.z = 0.2
        angular_speed = vel_msg.angular.z
        relative_angle = angle*PI/180
        #velocity_publisher.publish(vel_msg)
        t0 = rospy.Time.now().to_sec()
        current_angle = 0
        while(current_angle < relative_angle):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed*(t1-t0)


        #Forcing our robot to stop
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        

    while not rospy.is_shutdown():
        move_forward(2, vel_msg)
        vel_msg.linear.x = 0
        turn_left(90, vel_msg)
        #Setting the current time for distance calculus
        
    

if __name__ == '__main__':
    try:
        #Testing our function
        square_openloop()
    except rospy.ROSInterruptException: pass

