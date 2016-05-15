import EX106
import time
import readIMU

servo1max = 3575
servo1min = 711
servo2max = 1858
servo2min = 113

#将电机的数据直接转化为sync_write可以读的格式
def generate_servo(id,position,speed):
	return [id ,position&0xFF,position>>8,speed&0xFF,speed>>8]

def write_goal(id, position, speed = 0x40):
	if id == 1:
		if position > servo1max:
			position = servo1max
			print "exceed servo1 max"
		elif position < servo1min:
			position = servo1min
			print "exceed servo1 min"
	elif id == 2:
		if position > servo2max:
			position = servo2max
			print "exceed servo2 max"
		elif position < servo2min:
			position = servo2min
			print "exceed servo2 min"
	servo = generate_servo(id,position,speed)
	EX106.syncWrite(0x1E,servo)

#该函数用来控制2个电机，速度默认为0x40较慢，可以直接给两个电机写位置,前提是不超出电机转动范围
def sync_write_goal(id1,position1,id2,position2,speed1=0x40,speed2=0x40):
	servo1 = 0
	servo2 = 0
	if position > servo1max:
		position = servo1max
		print "exceed servo1 max"
	elif position < servo1min:
		position = servo1min
		print "exceed servo1 min"
	else
		servo1 = generate_servo(id1,position1,speed1)
	if position > servo2max:
		position = servo2max
		print "exceed servo2 max"
	elif position < servo2min:
		position = servo2min
		print "exceed servo2 min"
	else
		servo2 = generate_servo(id2,position2,speed2)
	if ((servo1 != 0)&&(servo2 != 0)):
		EX106.syncWrite(0x1E,servo1,servo2)

#该函数用于保持头部平衡
def keep_position(target,pose):
	if abs(pose[1] - target [1])< 10:
		pitchAdd = 0
	else
		pitchAdd = target[1] - pose[1]
	if abs(pose[2] - target [2])< 10:
		yawAdd = 0
	else
		yawAdd = target[2] - pose[2]
	current_pitch += pitchAdd
	current_yaw += yawAdd
	sync_write_goal(1,current_yaw,2,current_pitch)


if __name__ == '__main__':
	target = [0,0x800，0x800]#roll pitch yaw,其中roll没用
  while True:
  	pose = readIMU.readData()
  	keep_position(target,pose)
