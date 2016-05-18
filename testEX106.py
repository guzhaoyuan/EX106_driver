import EX106

#EX106.write(1,3,0x1E,255,7)#write target position to specific ID on daisy chain
#EX106.ping(1)#ping a specific ID on daisy chain
EX106.scan()#scan motor on daisy chain

#create some motor to write to daisy chain
servo1 = [0,0x10,0x00,0x20,0x00]
servo2 = [1,0x00,0x07,0x00,0x03]
servo3 = [2,0x00,0x07,0x00,0x03]
servo4 = [3,0x20,0x02,0x80,0x03]
#write to multi motor with different IDs on the same daisy chain
EX106.syncWrite(0x1E,servo1,servo2,servo3)
