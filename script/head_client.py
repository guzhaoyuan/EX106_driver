#!/usr/bin/env python

import sys
import rospy
import time
from gait.srv import head_decision

position_max = 151875 #151875 = 180 degree ; -151875 = -180 degree
soft_limit = 2000 #

#because the /head_decision is upside-down, so here we put yaw as first parameter
def sync_write_angel_client(yaw_angel, pitch_angel,duration):#tobe test
    yaw = yaw_angel * position_max / 180
    pitch = pitch_angel * position_max / 180
    sync_write_position_client(yaw,pitch,duration)

def sync_write_position_client(yaw, pitch,duration):#tested
    rospy.wait_for_service('head_service')

    if yaw_angel > soft_limit:
        yaw_angel = soft_limit
    elif yaw_angel < -soft_limit:
        yaw_angel = -soft_limit
    if pitch_angel > soft_limit:
        pitch_angel = soft_limit
    elif pitch_angel < -soft_limit:
        pitch_angel = -soft_limit

    try:
        sync_write = rospy.ServiceProxy('head_service', head_decision)
        result = sync_write(yaw, pitch,duration)
        return result
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

#def usage():
#    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    print "result = %s"%(sync_write_position_client(1000, 1000,0))
    time.sleep(2)
    print "result = %s"%(sync_write_position_client(1000, -1000,0))
    time.sleep(2)
    print "result = %s"%(sync_write_position_client(-1000, -1000,0))
    time.sleep(2)
    print "result = %s"%(sync_write_position_client(-1000, 1000,0))
    time.sleep(2)