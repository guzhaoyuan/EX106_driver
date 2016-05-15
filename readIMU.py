# -*- coding: utf-8 -*- 

import serial
import time
import binascii

IMUser = serial.Serial('/dev/tty.usbmodem1411',57600,timeout=0.025)

def readData():
	data = ""
	while (IMUser.read() != '!'):
		pass#print(IMUser.read())
	ch = IMUser.read()
	while (ch != '*'):
		#print(ch)
		data += ch
		ch = IMUser.read()
	result = parseData(data)
	#print(result)
	return result	#roll pitch yaw

def flush():
	IMUser.flushOutput()
	IMUser.flushInput()

def parseData(data):
	result = data.split(",")
	for num in range(0,3):
		result[num] = float(result[num])
	return result

if __name__ == '__main__':
	while True:
		pose = readData()
		print(pose)