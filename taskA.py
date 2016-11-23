import time
import ev3dev.ev3 as ev3
import math
import utilities as util


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
    offset = 45                           # target color value from calibrate
    Tp = 24                               # target duty_cycle value
    lowerBound = 0
    higherBound = 80

    lowestError = lowerBound - offset
    # Kp = float(0 - Tp)/float(lowestError - offset)
    Kp = 26
    Ki = 0
    Kd = 0
    lastError = 0
    integral = 0


    # left-right adjustable function that moves towards edge according to color
    def moving(left,right,c,lastError, integral):
        counter = 0
        while(counter < 11):
            color = c.value()
            print("Current color is: " + str(color))
            error = color - offset
            print("Error: " + str(error))

            integral = integral + error
            print("Integral: " + str(integral))
            derivative = error - lastError
            print("Derivative: " + str(derivative))

            # exit statement when white is consistently detected
            if (abs(derivative) < 5 and color > 82):
                counter += 1

            turn = Kp*error + Ki*integral + Kd*derivative
            turn = turn/100
            print("Turn: " + str(turn))

            powerL = Tp - turn                 # the power level for the motorL
            powerR = Tp + turn                 # the power level for the motorR
            print("powerL: " + str(powerL))
            print("powerR: " + str(powerR))
            left.run_timed(duty_cycle_sp = powerL, time_sp = 150)
            right.run_timed(duty_cycle_sp = powerR, time_sp = 150)

            time.sleep(.1)
            lastError = error               # save the current error so it can be the lastError next time
            print('----------------------------', counter)
        ev3.Sound.speak('finished following line').wait()
        print ('finished following line')

    # white on the right, following outer edge
    moving(motorL,motorR,c,lastError, integral)

    #white on left, following inside edge
    # moving(motorr,motorl,c)
    print('done with line following!!')




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
