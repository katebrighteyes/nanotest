# !/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node("topic_pub")
# define node name as 'topic_pub'

pub = rospy.Publisher("test_string", String) 
# give name test_string to the topic

rate = rospy.Rate(2) 

while not rospy.is_shutdown():
    pub.publish("Hello ROS")
    rate.sleep()
