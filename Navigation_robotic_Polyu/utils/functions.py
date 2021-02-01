import cv2
import time

def find_centroid(c):
    M = cv2.moments(c)
    # calculate x,y coordinate of center
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    return cX,cY

def reset_FT300(rob, wait=True):
    prg = '''def prog():
    if(socket_open("127.0.0.1",63350,"acc")): 
        socket_send_string("SET ZRO","acc")
        sleep(0.1)
        socket_close("acc")
    end
end
'''
    print("FT300 reset")
    programString = prg
    rob.send_program(programString)
    time.sleep(0.25)