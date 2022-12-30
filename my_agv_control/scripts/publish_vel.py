import rospy
from geometry_msgs.msg import Twist
i = 1
def publisher():
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	rospy.init_node('cmd_vel_array_publisher')
	rate = rospy.Rate(0.1)
	cmd_vel_array = [0.2, 0.3, 0.5, 0.4, 0.3]
	vel = Twist()
	while not rospy.is_shutdown():
		for i in range(len(cmd_vel_array)):
			vel.linear.x = cmd_vel_array[i]
			print("Publishing v = " + str(cmd_vel_array[int(i)]))
			pub.publish(vel)
			i = i + 1
			rate.sleep()
		# vel.linear.x += i
		# pub.publish(vel)
		# rate.sleep()

if __name__ == '__main__':
	publisher()	
