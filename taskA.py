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
    c = ev3.ColorSensor(ev3.INPUT_3)
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
            if(color < 15):
                print('black', color)
                left.run_timed(duty_cycle_sp=35, time_sp=150)
                # while 'running' in left.state:
                #     print left.state
                #     time.sleep(0.1)
                time.sleep(.15)
                counter += 1
            elif(color > 50):
                print('white', color)
                right.run_timed(duty_cycle_sp=35, time_sp=150)
                time.sleep(.15)
                counter += 1
            else:
                print('edge', color)
                left.run_timed(duty_cycle_sp=35, time_sp=200)
                right.run_timed(duty_cycle_sp=35, time_sp=200)
                time.sleep(.15)
                counter += 1


    # white on the right, following outer edge
    moving(motorl,motorr,c)

    #white on left, following inside edge
    # moving(motorr,motorl,c)
    print('done with line following!!')
