#!/usr/bin/env python
import rospy

from motor_control.DCmotor_HAT import DCmotor_HAT



class DCmotorNode(object):
    def __init__(self):
        a=1 
        #print("hi")
        self.motor = DCmotor_HAT()
        
        #print("start")

if __name__ == '__main__':                                                      
    rospy.init_node('DCmotor_node', anonymous=False)
    DCmotor_node = DCmotorNode()
    rospy.loginfo("init node\n")
    rospy.spin()
