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
    offset = 40                           # target color value
    Tp = 30                               # target duty_cycle value
    lowerBound = 0
    higherBound = 80

    lowestError = lowerBound - offset
    Kp = float(0 - Tp)/float(lowestError - offset)
    print('Kp: ', str(Kp))
    time.sleep(3)
    # Ki = 0
    # Kd = 0
    integral = 0
    lastError = 0
    # derivative = 0

    # left-right adjustable function that moves towards edge according to color
    def moving(left,right,c):
        counter = 0
        while(counter < 150):
           color = c.value() # what is the current light reading?
           print("Current color is: " + str(color))

           error = color - offset          # calculate the error by subtracting the offset
           print("Error: " + str(error))

           integral = integral + error        # calculate the integral (sum of all errors)
           # print("Integral: " + integral)
           # derivative = error - lastError     # calculate the derivative (rate of change of error)
           # print("Derivative: " + derivative)

           turn = Kp*error
           # + Ki*integral + Kd*derivative  # the "P term" the "I term" and the "D term"
           # turn = Turn/100                    # REMEMBER to undo the affect of the factor of 100 in Kp, Ki and Kd!
           print("Turn: " + str(turn))

           powerL = Tp - turn                 # the power level for the motorL
           powerR = Tp + turn                 # the power level for the motorR
           print("powerL: " + str(powerL))
           print("powerR: " + str(powerR))

           left.run_timed(duty_cycle_sp = powerL, time_sp = 150)
           right.run_timed(duty_cycle_sp = powerR, time_sp = 150)
           time.sleep(.1)
           counter += 1
           lastError = error                  # save the current error so it can be the lastError next time around



    # white on the right, following outer edge
    moving(motorL,motorR,c)

    #white on left, following inside edge
    # moving(motorr,motorl,c)
    print('done with line following!!')
