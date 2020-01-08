# ROS melodic

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

sudo apt update

sudo apt install ros-melodic-desktop

sudo rosdep init

rosdep update


# workspace 만들기 


# pub sub 예제

cd ~/catkinws/src 

catkin_create_pkg test_ros_pkg std_msgs rospy

