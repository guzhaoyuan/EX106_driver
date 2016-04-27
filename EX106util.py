import EX106

servo1max = 3575
servo1min = 711
servo2max = 1858
servo2min = 113

def write_goal(id, position, speed = 0x3FF):
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
	servo = [id ,position&0xFF,position>>8,speed&0xFF,speed>>8]
	EX106.syncWrite(0x1E,servo)

def sync_write_goal(id1,position1,id2,position2,speed1=0x3FF,speed2=0x3FF):
	servo1 = [id1, position1&0xFF,position1>>8,speed1&0xFF,speed1>>8]
	servo2 = [id2, position2&0xFF,position2>>8,speed2&0xFF,speed2>>8]
	EX106.syncWrite(0x1E,servo1,servo2)

write_goal(1,1000)