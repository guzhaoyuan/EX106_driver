# -*- coding: utf-8 -*- 

import serial
import time
import binascii

IMUser = serial.Serial('/dev/tty.wchusbserial1421',57600,timeout=0.25)

def readData():
	data = ser.read(size=20)
	result = parseData(data)
	return result	#roll pitch yaw

def parseData(data):
	return data