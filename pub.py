#!/usr/bin/python3

import rospy 
from std_msgs.msg import String 

def publisher():
    rospy.init_node("helon_node1",anonymous=True)
    pub=rospy.Publisher('greetings',String,queue_size=20)
    rate=rospy.Rate(10)
    #rospy.loginfo("")

    while not rospy.is_shutdown():
        txt="hello,i am helon"
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

 