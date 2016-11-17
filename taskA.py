import time
import ev3dev.ev3 as ev3
import math
import utilities as util

def PID():

Kp = 1000                             # REMEMBER we are using Kp*100 so this is really 10 !
Ki = 100                              # REMEMBER we are using Ki*100 so this is really 1 !
Kd = 10000                            # REMEMBER we are using Kd*100 so this is really 100!

offset = 45                           # target value (45 = go straight)
Tp = 50                               # target power

integral = 0                          # the place where we will store our integral
lastError = 0                         # the place where we will store the last error value
derivative = 0                        # the place where we will store the derivative

while True:

   lightVal = ev3.ColorSensor.value() # what is the current light reading?
   print("Current color is: " + lightVal)

   error = lightVal - offset          # calculate the error by subtracting the offset
   print("Error: " + error)

   integral = integral + error        # calculate the integral (sum of all errors)
   print("Integral: " + integral)

   derivative = error - lastError     # calculate the derivative (rate of change of error)
   print("Derivative: " + derivative)
   
   Turn = Kp*error + Ki*integral + Kd*derivative  # the "P term" the "I term" and the "D term"
   Turn = Turn/100                    # REMEMBER to undo the affect of the factor of 100 in Kp, Ki and Kd!
   print("Turn: " + turn)

   powerL = Tp + Turn                 # the power level for the motorL
   powerR = Tp - Turn                 # the power level for the motorR
   motorL.run_timed(duty_cycle_sp = powerL, ...)
   motorR.run_timed(duty_cycle_sp = powerR, ...)

   lastError = error                  # save the current error so it can be the lastError next time around
                                      # done with loop, go back and do it again.

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
