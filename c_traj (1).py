#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
pose=0

def callback(msg):
	global pub,pose,radius
	pose=msg.pose.pose.position.x
		
	vel=Twist()
	vel.angular.z=1
	vel.linear.x=radius
	
	
	rospy.Rate(1)	
	pub.publish(vel)
	
	print(pose)

def listener():
	global pub,vel,pose
	
	rospy.init_node("circle_rad")

	pub=rospy.Publisher('/cmd_vel',Twist, queue_size=1)
	
	rospy.Subscriber('/odom',Odometry,callback)
	
	rospy.spin()


if __name__ == '__main__':
	try:
		global radius		
		radius=float(input("Enter the required radius: "))
		listener()
	except rospy.ROSInterruptException:
		pass




