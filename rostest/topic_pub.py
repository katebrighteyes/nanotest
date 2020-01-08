# !/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node(‘topic_pub’)
# 노드 이름을 topic_pub로 정의한다.

pub = rospy.Publisher(‘test_string’, String) 
# 토픽에 test_string 이라는 이름을 부여한다.

rate = rospy.Rate(2) #발행 속도는 초당 2번

while not rospy.is_shutdown():
    pub.publish(‘AAA-BBB')
    rate.sleep()
