# !/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):  # 콜백 함수 정의
    print msg.data

rospy.init_node(‘topic_sub’) 
# 노드 이름을 topic_sub로 정의한다.

sub = rospy.Subscriber(‘test_string’, String, callback)
# test_string 토픽 처리를 위한 callback함수 등록

rospy.spin() 
# ROS에게 제어를 넘긴다. 노드가 종료할 경우 리턴된다.
