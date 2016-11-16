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
    def moving(left,right,c):
        counter = 0
        while(counter < 150):
            color = c.value()
            if(color < 20):
                print('black')
                left.run_timed(duty_cycle_sp=35, time_sp=150)
                time.sleep(.15)
                counter += 1
            elif(color > 60):
                print('white')
                right.run_timed(duty_cycle_sp=35, time_sp=100)
                time.sleep(.15)
                counter += 1
            else:
                print('edge')
                left.run_timed(duty_cycle_sp=40, time_sp=200)
                right.run_timed(duty_cycle_sp=40, time_sp=200)
                time.sleep(.15)
                counter += 1


    # designing for outer edge, white on the right, can invert them if
    moving(motorl,motorr,c)

    print('done with line following!!')
