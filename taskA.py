#! /usr/bin/env python
# Core imports
import time
import ev3dev.ev3 as ev3


def followline_PID():
    # connecting motors and senors
    motorL =ev3.LargeMotor('outA')
    motorL.connected
    motorR =ev3.LargeMotor('outD')
    motorR.connected
    c = ev3.ColorSensor(ev3.INPUT_3)
    c.connected
    c.mode = 'COL-REFLECT'

    # Constants for PID
    offset = 45                           # target color value when on line edge
    Tp = 24                               # target duty_cycle value
    # lowerBound = 0
    # lowestError = lowerBound - offset
    # Kp = float(0 - Tp)/float(lowestError - offset)
    Kp = 26
    Ki = 0
    Kd = 0
    lastError = 0
    integral = 0

    # left-right adjustable function that moves towards edge according to color
    def moving(left,right,c,lastError, integral):
        # counter keeps track of how long color sensor is only detecting white
        counter = 0
        # while it's not consistently detecting white, it must be on the line
        while(counter < 11):
            color = c.value()
            error = color - offset
            integral = integral + error
            derivative = error - lastError

            # exit statement when white is consistently detected
            if (abs(derivative) < 5 and color > 82):
                counter += 1

            turn = Kp*error + Ki*integral + Kd*derivative
            turn = turn/100
            powerL = Tp - turn                 # the power level for the motorL
            powerR = Tp + turn                 # the power level for the motorR

            left.run_timed(duty_cycle_sp = powerL, time_sp = 150)
            right.run_timed(duty_cycle_sp = powerR, time_sp = 150)
            time.sleep(.1)

            lastError = error            # save the current error for derivative

        ev3.Sound.speak('finished following line').wait()
        print ('finished following line')

    # white on the right, following outer edge
    moving(motorL,motorR,c,lastError, integral)

    #white on left, following inside edge
    # moving(motorr,motorl,c)




# brute-force version of followline
def followline():
    # connecting motors and senors
    motorl =ev3.LargeMotor('outA')
    motorl.connected
    motorr =ev3.LargeMotor('outD')
    motorr.connected
    c = ev3.ColorSensor(ev3.INPUT_3)
    c.connected
    c.mode = 'COL-REFLECT'

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

    moving(motorl,motorr,c)

followline_PID()

time.sleep(5)
