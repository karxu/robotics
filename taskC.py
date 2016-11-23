import time
import ev3dev.ev3 as ev3
import math
import utilities as util
import detector as detector




def aroundObstacle():
    # connecting motors
    motorL =ev3.LargeMotor('outA')
    motorL.connected
    motorR =ev3.LargeMotor('outD')
    motorR.connected
    motorM =ev3.MediumMotor('outB')
    motorM.connected

    # declare color sensor
    c = ev3.ColorSensor(ev3.INPUT_3)
    c.connected
    c.mode = 'COL-REFLECT'

    # declare sonar
    sonar = ev3.UltrasonicSensor(ev3.INPUT_4)
    sonar.connected
    sonar.mode = 'US-DIST-CM'

    def circumvent():
        prev_val = 0;       # keeps track of previous sonar value
        diff = 0;           # keeps track of diff btwn current val and prev val

        print('turning left')
        turnL()
        moveForward()

        time.sleep(1)
        colorVal = c.value()
    # Onji's brute force logic
        # while (colorVal > 15):
        #
        #     # calculate difference
        #     moveForward()
        #     diff = sonar.value() - prev_val
        #     print("Diff: " + str(diff))
        #
        #     # if the diff > 290, that means you reached the edge of the obstacle
        #     # ie. WALL = 30, NO WALL = 900, DIFF = 870
        #     if( (abs(diff) > 290) ):
        #         ev3.Sound.speak('Turning right').wait()
        #         turnR()
        #         time.sleep(1)
        #         prev_val = sonar.value()
        #         colorVal = c.value()
        #
        #     else:
        #         prev_val = sonar.value()
        #         colorVal = c.value()

    # PID logic
        offset = 80
        Tp = 30
        Kp = 12
        Ki = 0
        Kd = 0

        lastError = 0
        integral = 0

        while (c.value() > 15):
            s = sonar.value()
            print("Current sonar is: " + str(s))

            error = s - offset
            print("Error: " + str(error))
            integral = integral + error
            derivative = error - lastError

            turn = Kp*error + Ki*integral + Kd*derivative
            turn = turn/1000
            print("turn: " + str(turn))

            powerL = Tp + turn                 # the power level for the motorL
            powerR = Tp - turn                 # the power level for the motorR
            print("powerL: " + str(powerL))
            print("powerR: " + str(powerR))
            motorL.run_timed(duty_cycle_sp = powerL, time_sp = 150)
            motorR.run_timed(duty_cycle_sp = powerR, time_sp = 150)
            lastError = error
            time.sleep(.1)

            print('----------------------------')

        # when color sensor is no longer reading white, turn and move forward
        ev3.Sound.speak('Found black line again').wait()
        print('Found black line again')
        turnL()
        moving()





    def moving():
        # Constants for PID
        offset = 45
        Tp = 25
        Kp = 25

        # move forward until sonar detects object
        while(sonar.value() > 250 ):
           color = c.value()
           error = color - offset
           turn = Kp*error
           turn = turn/100

           powerL = Tp - turn                 # the power level for the motorL
           powerR = Tp + turn                 # the power level for the motorR

           motorL.run_timed(duty_cycle_sp = powerL, time_sp = 150)
           motorR.run_timed(duty_cycle_sp = powerR, time_sp = 150)

           time.sleep(.1)

        # then switch to circumvent function
        ev3.Sound.speak('Obstacle Detected').wait
        time.sleep(1)
        circumvent()



    def turnR():
        print("turn right")
        motorL.run_timed(duty_cycle_sp = 40, time_sp=3000)
        motorR.run_timed(duty_cycle_sp = 15, time_sp=3000)
        time.sleep(.2)


    def turnL():
        print("turn left")
        motorR.run_timed(duty_cycle_sp = 60, time_sp=3000)
        motorL.run_timed(duty_cycle_sp = -60, time_sp=3000)
        time.sleep(.2)
        motorM.run_timed(duty_cycle_sp = 30, time_sp=800)
        time.sleep(.2)


    # moves forward
    def moveForward():
        motorL.run_timed(duty_cycle_sp=25, time_sp=800)
        motorR.run_timed(duty_cycle_sp=25, time_sp=800)
        time.sleep(0.5)

    moving()
