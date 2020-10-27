import rospy
from std_msgs.msg import String

rospy.init_node('teste2')

matricula='0'

def function_msg(event):
    global matricula
    matricula = event.data

sub = rospy.Subscriber('/topic1', String, function_msg)

def timerCallBack(event):

    sum_matricula = 0
    for digit in matricula:
        sum_matricula +=int(digit)
    msg = String()
    msg.data = str(sum_matricula)
    pub.publish(msg)

pub = rospy.Publisher('/topic2', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin()