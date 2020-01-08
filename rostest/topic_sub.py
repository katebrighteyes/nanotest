# !/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):  # callback function
    print msg.data

rospy.init_node("topic_sub") 
# define node name "topic_sub"

sub = rospy.Subscriber("test_string", String, callback)
# Register callback function for test_string topic

rospy.spin() 

