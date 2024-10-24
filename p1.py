#!/usr/bin/python3

import rospy 
from std_msgs.msg import String 

def publisher():
    rospy.init_node("helon",anonymous=True)
    pub=rospy.Publisher('hello_class',String,queue_size=20)
    sub=rospy.Subscriber("welcome",String)
    rate=rospy.Rate(10)
    #rospy.loginfo("")

    while not rospy.is_shutdown():
        txt="hello RAA24_26!"
        msg=String()
        msg.data=txt
        pub.publish(msg)
        rospy.loginfo(msg.data)
        rate.sleep()

if __name__=='__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass