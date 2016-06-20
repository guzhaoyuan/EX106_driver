# -*- coding: utf-8 -*- 

from time import sleep
import serial

port = '/dev/ttyACM0'
#port = '/dev/tty.wchusbserial1420' #for Mac
ser = serial.Serial(port, baudrate=57600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

while True:
     print ser.readline() # Read the newest output from the Arduino
     sleep(.01) # Delay for one tenth of a second
