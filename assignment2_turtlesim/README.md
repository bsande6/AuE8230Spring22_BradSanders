Assignment 2: Git and TurtleSim

Part 1: circle.py
This script moves the turle in a circle with a linear velocity of 0.5 and an angular velocity of 0.5
To make the turtle move in a circle first launch the simulation with 

rosrun turtlesim turtlesim_node

Then run the circle script with

rosrun assignment2_ws circle.py
![circle.py](/docs/images/circle_trajectory.png)

Part 2: square_openloop.py
This script moves the turtle in a square without position feedback for the turtle. The distance traveled is calculated by measuring the speed and time. The turtle moves with linear and angular velocities equal to 0.2

rosrun turtlesim turtlesim_node
rosrun assignment2_ws square_openloop.py
![square_openloop.py](/docs/images/square_openloop_trajectory.png)

Part 3: square_closedloop.py
The turtle moves in a square but it is able to determine its position by listening to the pose topic.
To run this script first launch turtlesim then reposition the turtle using the following commands.

rosrun turtlesim turtlesim_node
rosservice call /kill "name: 'turtle1'"
rosservice call /spawn "x: 5.0
			y:5.0
			theta: 0.0
			name: 'turtle1'"
rosrun assignment2_ws square_closedloop.py
![square_openloop.py](/docs/images/square_closedloop_trajectory.png)
