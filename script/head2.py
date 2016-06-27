#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import time
import readIMU
import pid
import rospy
import head_client
from operator import add
from Head.msg import head_pose 
#from gait.msg import head_angle_msg
from Head.srv import head_control
from Head.msg import head_servo_angel


Pi = 3.1415926
#publish msg to head_angel.msg
pub_imu = rospy.Publisher('Head/head_angle',head_pose,queue_size=101)
#init a node
rospy.init_node('Head_data',anonymous=True)

#读num组数据做平均做出初始值
def get_average_IMU(num):
	pose = [0,0,0]
	for num in range(1,num+1):
		pose = map(add, pose, readIMU.readData())
	pose[:] = [x / num for x in pose]
	return pose

#主函数
if __name__ == '__main__':
	target = [0,0,0]#pitch roll yaw,其中roll没用

	for num in range(1,100): #读200组数据扔掉
		pose = readIMU.readData()
	
	target = get_average_IMU(10) #读10组数据做平均做出初始值
	
	while True:
		temp = get_average_IMU(2) #读4组数据做平均作为当前姿态
		pub_imu.publish(temp[2],temp[0])
		readIMU.flush()
