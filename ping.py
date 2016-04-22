import serial
import time
import binascii

ser = serial.Serial('/dev/tty.usbserial',57600,timeout=0.25)
#ser = serial.Serial('/dev/tty.wchusbserial1420',57600,timeout=0.25)

def checksum(data):
    data = 0xFF & data
    crc = ~(data)

    if (crc <= 0x0F):
        crc = crc & 0xFF
    return crc

def parse(pack):
	print 'id='+pack[4:6]
	print 'error='+pack[8:10]

addr = 0x01
length = 0x02
inst = 0x01
crc = checksum(addr + length + inst)
data = [addr,length,inst,crc]
package = "".join(map(chr,[0xFF,0xFF] + data))

ser.flushOutput();
ser.flushInput();
#ser.write(package)
time.sleep(0.1)
ser.write(package)

while True:
	respond = ser.read(size=6)
	#res= [map(ord, x) for x in respond]
	res= binascii.hexlify(respond) 
	print res
	if res != '':
		parse（res）
#ser.close()