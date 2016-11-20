import time
import ev3dev.ev3 as ev3
import math
import utilities as util

def calibrate():
    c = ev3.ColorSensor(ev3.INPUT_3)
    c.connected
    c.mode = 'COL-REFLECT'

    ev3.Sound.speak('Place robot on white').wait()
    print('Place on white')
    time.sleep(3)
    white1 = c.value()
    print(white1)
    ev3.Sound.speak('Place robot on another white').wait()
    print('Place on another white')
    time.sleep(3)
    white2 = c.value()
    print(white2)


    ev3.Sound.speak('Place robot on black').wait()
    print('Place on black')
    time.sleep(3)
    black1 = c.value()
    print(black1)
    ev3.Sound.speak('Place robot on another black').wait()
    print('Place on another black')
    time.sleep(3)
    black2 = c.value()
    print(black2)

    offset = (white1 + white2 + black1 + black2)/4
    print('OFFSET' + str(offset))
    time.sleep(10)



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
    offset = 30                           # target color value from calibrate
    Tp = 30                               # target duty_cycle value
    lowerBound = 0
    higherBound = 80

    lowestError = lowerBound - offset
    Kp = float(0 - Tp)/float(lowestError - offset)
    print('Kp: ', str(Kp))
    time.sleep(3)
    Ki = 0
    Kd = 0
    lastError = 0
    integral = 0


    # left-right adjustable function that moves towards edge according to color
    def moving(left,right,c,lastError, integral):
        counter = 0
        while(counter < 200):
           color = c.value()
           print("Current color is: " + str(color))

           error = color - offset          # calculate the error by subtracting the offset
           print("Error: " + str(error))

# Jenn: add in integral and derivative
           integral = integral + error        # calculate the integral (sum of all errors)
           print("Integral: " + str(integral))
        #    derivative = error - lastError     # calculate the derivative (rate of change of error)
        #    print("Derivative: " + str(derivative))

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
           lastError = error               # save the current error so it can be the lastError next time
           print('----------------------------', counter)

    # white on the right, following outer edge
    moving(motorL,motorR,c,lastError, integral)

    #white on left, following inside edge
    # moving(motorr,motorl,c)
    print('done with line following!!')
