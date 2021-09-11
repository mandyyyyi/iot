import picar_4wd as fc
import time, math
import threading

import cv2
from speed import Speed
from picar_4wd.pwm import PWM
from picar_4wd.servo import Servo


speed = 20
# def reset_servo(angle1):
#     ser = Servo(PWM("P0"))                     
#     ser.set_angle(angle1) 

def main():

    # reset_servo(-65)
    ser = Servo(PWM("P0"))                     
    ser.set_angle(-65)
    while True:
        scan_list = fc.scan_step(25)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(tmp)
        if tmp != [2,2,2,2]:        
         
          fc.stop()
          time.sleep(0.4)
          fc.backward(80)
          time.sleep(0.4)
          fc.stop()
          time.sleep(0.4)
          fc.turn_right(40)   
        else:
          fc.forward(speed)

if __name__ == "__main__":
    main()
