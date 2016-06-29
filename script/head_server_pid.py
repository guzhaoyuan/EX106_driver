#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import time
#import readIMU
import pid
import rospy
import head_client
from operator import add
#from gait.msg import head_angle_msg
from Head.srv import head_control
from Head.msg import head_servo_angel
from Head.msg import head_pose

Pi = 3.1415926

#servo init angel
init_pitch = 0
init_yaw = 0

#当前的位置
#初始化时，当前位置等于初始位置
current_pitch = init_pitch
current_yaw = init_yaw

#变量控制是否进行PID
init_PID = 0
#初始化目标角度
target = [0,0,0]#pitch roll yaw


#该函数用于保持头部平衡
def keep_position(target,pose):
	print("target= "),
	print(target),
	print("pose= "),
	print(pose)
	if abs(pose[0] - target[0])< 3:
		pitchAdd = 0
	else:
		pitchAdd = target[0] - pose[0]
	if abs(pose[2] - target[2])< 3:
		yawAdd = 0
	else:
		yawAdd = target[2] - pose[2]

	global current_pitch
	global current_yaw
	offset = pid.calc_pid(target,pose)#得到输出的偏移值
	print(offset)
	if (abs(current_pitch) < head_client.soft_limit):
		current_pitch -= offset[0]#修改pitch输出
	if (abs(current_yaw) < head_client.soft_limit):
		current_yaw -= offset[2]#修改yaw输出

	print("command yaw:"),
	print(current_yaw),
	print("command pitch"),
	print(current_pitch)
#	sync_write_angel(1,current_yaw,2,current_pitch)
	head_client.sync_write_angel_client(current_yaw,current_pitch,0)
	pub_servo.publish(current_pitch,current_yaw)
	#send servo pose every after servo move

def callback(data):
	if init_PID == 0:#如果不需要PID，则传来的msg用于更新target
		target = [data.pitch,0,data.yaw]
	else:#一旦需要PID，将target设为目标角度
		pose = [data.pitch,0,data.yaw]
		keep_position(target,pose)

#callback function receive pitch[-Pi/2,Pi/2] and yaw[-Pi,Pi] and call security service directly
def handle_head_control(req):
	pitch = (req.pitch)
	yaw = (req.yaw)
	head_client.sync_write_angel_client(yaw,pitch,0)
	pub_servo.publish(pitch,yaw)
	init_PID = req.PID
	return 0

#server init, receive yaw and pitch
def head_control_server():
	#publish msg to head_servo_angel.msg 
	rospy.init_node('head_control_server')
	s = rospy.Service('head_control_withPID',head_control,handle_head_control)
	print "head control server ready"
	rospy.spin()

#publish msg to head_servo_angel.msg 
pub_servo = rospy.Publisher('Head/head_servo_angel',head_servo_angel,queue_size=100)

#建立一个listener
rospy.Subscriber('Head/head_angle', head_pose, callback)


#主函数
if __name__ == '__main__':
	try:
		head_control_server()	
	except rospy.ROSInterruptException:
		pass
