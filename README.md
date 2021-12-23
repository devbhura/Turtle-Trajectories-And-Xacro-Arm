# HW2 - ME 495


# Overview
Part 1:
Makes the robot move in a figure 8 shape. The robot starts moving when launched on a real turtlebot3 and can be paused and resumed.

Part 2: 
Defines a two arm robot with an end effector. When launched the robot arm moves in a trajectory and also shows markers at the end effector in rviz


# Usage 

Part 1:

There are two modes for this robot. To launch the sim version, one can run `roslaunch homework2 figure_eight.launch mode:=sim`. 

The math tat defines the figure 8 trajectory can be seen in the `math.py` file in `src/homework2`

Below are the expected results:

![turtlesim](https://user-images.githubusercontent.com/55405657/138229320-5e58fac5-5860-45d7-8cf9-9e5262c914ac.gif)

![rviz_turtle](https://user-images.githubusercontent.com/55405657/138229346-926d6997-05a1-4212-b5ba-47d55d7e7a93.gif)



To make the real turtlebot3 move, run `roscore` on your computer and ssh into the turtlebot3. Set `ROS_MASTER_URI` and run `roslaunch turtlebot3_bringup turtlebot3_robot.launch` from the robot. Then run `roslaunch homework2 figure_eight.launch mode:=real` to make the robot move. You can use the `pause` service to pause and `resume` service to resume the robot. 

The robot is expected to move as follows:

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/55405657/138232131-4eac4b2c-affe-4880-a2fc-a71522f40dc7.gif)


Part 2:

Run `roslaunch homework2 arm_marker.launch` from the ws to run the arm in rviz with markers. 

Demo:
![arm_traj](https://user-images.githubusercontent.com/55405657/138230955-9e8eab08-8d2a-44f7-b9d9-c528903be1b3.gif)

