import time
import ev3dev.ev3 as ev3
import math
import utilities as util


################################################
## FUNCTION: detectObstacle ####################
## Robot either turns or moves forward until ###
## an object is detected #######################
################################################

def detectObstacle():

    #declare sonar
    sonar = ev3.UltrasonicSensor(ev3.INPUT_2)
    sonar.connected
    sonar.mode = 'US-DIST-CM'

    #declare motors
    motorL =ev3.LargeMotor('outA')
    motorL.connected
    motorR =ev3.LargeMotor('outD')
    motorR.connected

    Kp = 0.02                             # Kp = (0-TP)/(-1,050-0)
    Ki = 0                                # 0 for now
    Kd = 0                                # 0 for now

    offset = 1350                         # offset = (300+2400)/2 (avg)
    Tp = 25                               # target power

    integral = 0                          # the place where we will store our integral
    lastError = 0                         # the place where we will store the last error value
    derivative = 0                        # the place where we will store the derivative

    while True:

        sonarVal = sonar.value()                        # get sonar value
        print("Current val is: " + str(sonarVal))       # print sonar value

        if (sonarVal < 200):                            # if object detected is close enough
            print("Obstacle detected")                  # print
            break                                       # exit while loop
        
        elif (sonarVal < 600):                          # if object detected is fairly locse
            moveForward()                               # move forward
        
        else:                                           # if no object is deteced (too far)
          error = sonarVal - offset                     # calculate the error by subtracting the offset
          print("Error: " + str(error))                 # print error value

          # integral = integral + error                 # calculate the integral (sum of all errors)
          # print("Integral: " + integral)

          # derivative = error - lastError              # calculate the derivative (rate of change of error)
          # print("Derivative: " + derivative)

          turn = Kp*error                               # calculate turn value           
          # + Ki*integral + Kd*derivative
          print("Turn: " + str(turn))                   # print turn value

          powerL = Tp + turn                            # calculate power for motorL
          powerR = Tp - turn                            # calculate power for motorR
          
          motorL.run_timed(duty_cycle_sp = powerL, time_sp=100)     # turn
          motorR.run_timed(duty_cycle_sp = powerR, time_sp=100)     # turn

          lastError = error                             # save the current error so it can be the lastError next time around
                                                        # done with loop, go back and do it again.

################################################
## FUNCTION: obstacleFinder ####################
################################################

# def obstacleFinder():

#     # define motors
#     motorl =ev3.LargeMotor('outA')
#     motorl.connected
#     motorr =ev3.LargeMotor('outD')
#     motorr.connected

#     # define ultrasonic sensor
#     sonar = ev3.UltrasonicSensor(ev3.INPUT_2)
#     sonar.connected
#     sonar.mode = 'US-DIST-CM',

#     medmotor = ev3.MediumMotor('outB')
#     medmotor.connected
#     medmotor.reset
#     # medmotor.position_sp = 50

#     print("sonar value", sonar.value())
#     print("medmotor position", medmotor.position)

#     while True:
#         print('boo')
#         if (sonar.value() > 2000):
#             medmotor.run_timed(duty_cycle_sp=25, time_sp=800)
#             time.sleep(1)
#             medmotor.run_timed(duty_cycle_sp=-25, time_sp=800)
#             time.sleep(1)
#         else:
#             moveForward()
#             break

#     # while True:
#     #     # if sonar does not detect anything less than 300mm away
#     #     if (sonar.value() > 2400):
#     #         # print current distance value in mm
#     #         print(sonar.value()
#     #         # move forward
#     #         motorr.run_timed(duty_cycle_sp=25, time_sp=1000)
#     #         motorl.run_timed(duty_cycle_sp=25, time_sp=1000)
#     #     # else sonar does detect something less than 300mm away
#     #     else if (sonar.value < 300)
#     #     else:
#     #         # print
#     #         print("obstacle detected")
#     #         # turn left
#     #         motorr.run_timed(duty_cycle_sp=25, time_sp=2000)
#     #         #break
#     #         break

#     print("done")
#     time.sleep(1)


    def moveForward():
        print("moveForward ------------------------")

    # define motors
    motorl =ev3.LargeMotor('outA')
    motorl.connected
    motorr =ev3.LargeMotor('outD')
    motorr.connected

    # motor encoder
    # initial_pos_l = motorl.position
    # initial_pos_r = motorr.position
    # print("left initial position: ", motorl.position)
    # print("right initial position: ", motorr.position)

    # run_time takes milliseconds
    motorl.run_timed(duty_cycle_sp=25, time_sp=2000)
    motorr.run_timed(duty_cycle_sp=25, time_sp=2000)

    final_pos_l = motorl.position
    final_pos_r = motorr.position
    # print("left final position: ", final_pos_l)
    # print("right final position: ", final_pos_r)


    # print("moveForward done ------------------------")
    time.sleep(1)
    # why do we need this line above in order to get the motor to run????????


    def gyroReading():
        print("gyro ------------------------")

    # define motors
    motorl =ev3.LargeMotor('outA')
    motorl.connected
    motorr =ev3.LargeMotor('outD')
    motorr.connected

    # gryo reading
    g = ev3.GyroSensor(ev3.INPUT_4)
    g.connected
    g.mode = 'GYRO-ANG'

    #what to put here--------
    while not btn.backspace:
        print g.value()

    # run_time takes milliseconds
    motorl.run_timed(duty_cycle_sp=50, time_sp=4000)
    motorr.run_timed(duty_cycle_sp=50, time_sp=4000)


    print("gyro done ------------------------")
    time.sleep(1)
