# ROS melodic 설치

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

sudo apt update

sudo apt install ros-melodic-desktop

sudo rosdep init

rosdep update

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc

source ~/.bashrc

# 테스트

[TEST]

EXECUTE roscore 창을 새로 띄운 후 roscore 실행

$ roscore

turtle 또 다른 창에서 거북이 창 실행

$ rosrun turtlesim turtlesim_node

move 또 다른 창에서 키 동작 오퍼 기능 실행

$ rosrun turtlesim turtle_teleop_key


# workspace 만들기 

## installcatkinws.sh 를 실행시키기 위해 권한을 바꾸고(1회) 실행시킨다.

chmod 777 installcatkinws.sh

./installcatkinws.sh

## 확인

ls ~/catkin_ws


# pub sub 예제

cd ~/catkinws/src 

catkin_create_pkg test_ros_pkg std_msgs rospy

