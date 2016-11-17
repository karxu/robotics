import time
import ev3dev.ev3 as ev3
import math
import utilities as util

def followline():
    print('followline begin----------------')

    # connecting motors and senors
    motorl =ev3.LargeMotor('outA')
    motorl.connected
    motorr =ev3.LargeMotor('outD')
    motorr.connected
    c = ev3.ColorSensor(ev3.INPUT_1)
    c.connected
    c.mode = 'COL-REFLECT'

    # manual color testing to get values for black and white
    # counter = 0
    # while(counter < 20):
    #     counter += 1
    #     print(c.value())
    #     time.sleep(1)


    #lef-right adjustable function that moves towards edge according to color

    kp = 1.6
    ki = 1
    kd = 0

    tp = 35 #target
    def moving(left,right,c):
        counter = 0
        while(counter < 150):
            color = c.value()

            
            time.sleep(.15)
            counter += 1



    # white on the right, following outer edge
    moving(motorl,motorr,c)

    #white on left, following inside edge
    # moving(motorr,motorl,c)
    print('done with line following!!')
