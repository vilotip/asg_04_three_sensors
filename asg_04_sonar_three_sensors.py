#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Range

pub_topic1='/range_1'
pub_topic2='/range_2'
pub_topic3='/range_3'
sub_topic1='/scan_1'
sub_topic2='/scan_2'
sub_topic3='/scan_3'

def function(data,pub):
    range_msg=Range()
    range_msg.header.stamp=rospy.Time.now()
    range_msg.header.frame_id=data.header.frame_id
    #range_msg.header.frame_id='laser_link'
    range_msg.radiation_type=Range.ULTRASOUND
    range_msg.field_of_view=0.0698132
    range_msg.min_range=0.1
    range_msg.max_range=30.0
    range_msg.range=sum(data.ranges)/len(data.ranges)
    pub.publish(range_msg)
    
rospy.init_node('sonar_node', anonymous=True)
pub_1 = rospy.Publisher(pub_topic1, Range, queue_size=10)
pub_2 = rospy.Publisher(pub_topic2, Range, queue_size=10)
pub_3 = rospy.Publisher(pub_topic3, Range, queue_size=10)
rospy.Subscriber(sub_topic1, LaserScan, function, callback_args=pub_1)
rospy.Subscriber(sub_topic2, LaserScan, function, callback_args=pub_2)
rospy.Subscriber(sub_topic3, LaserScan, function, callback_args=pub_3)

rospy.spin()
