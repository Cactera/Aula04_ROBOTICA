import rospy
from std_msgs.msg import String


rospy.init_node('teste1')
back = 'Waiting'

def function_back(event):
    global back
    back = event.data

def timerCallBack(event):

    print(back)
    msg = String()
    msg.data = '2016001094'
    pub.publish(msg)


pub = rospy.Publisher('/topic1', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)
sub = rospy.Subscriber('/topic2', String, function_back)

rospy.spin()