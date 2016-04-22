# -*- coding: utf-8 -*- 
import serial
import time
import binascii

#ser = serial.Serial('/dev/tty.usbserial',57600,timeout=0.25)
ser = serial.Serial('/dev/tty.wchusbserial1420',57600,timeout=0.25)

def checksum(data):
    data = 0xFF & data
    crc = ~(data)

    if (crc <= 0x0F):
        crc = crc & 0xFF
    print "crc= "+str(int(crc))
    return crc

def parse(pack):
	if pack[0:2] == '00':
		pack = pack[2:]
	if pack[2:4] == 'ff':
		print 'id='+pack[4:6]
		print 'error='+pack[8:10]
	else:
		print 'id='+pack[2:4]
		print 'error='+pack[6:8]

def write(id,instr,*para):
	paras = list(para)
	total = id + len(paras) + 2 + instr + sum(paras)
	crc = checksum(total)
	data =[id,len(paras)+2,instr]
	data += paras
	data.append(crc)
	package = "".join(map(chr,[0xFF,0xFF] + data))
	ser.flushOutput();
	time.sleep(0.1)
	ser.write(package)
	respond = ser.read(size=7)
	res= binascii.hexlify(respond) 
	parse(res)


addr = 0x01
length = 0x05
instr = 0x03
parameter1 = 0x1E
parameter2 = 0x00
parameter3 = 0x00
crc = checksum(addr + length + instr + parameter1 + parameter2 + parameter3)
data = [addr,length,instr,parameter1,parameter2,parameter3,crc]
package = "".join(map(chr,[0xFF,0xFF] + data))



ser.flushOutput();
ser.flushInput();
#ser.write(package)
#time.sleep(0.1)
#ser.write(package)

#while True:
#respond = ser.read(size=7)
	#res= [map(ord, x) for x in respond]
#res= binascii.hexlify(respond) 
#print res
	#if res.strip():
#parse(res)
#ser.close()