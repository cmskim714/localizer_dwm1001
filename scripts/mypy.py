#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    rospy.init_node('nav')
    print(rospy.get_name())

