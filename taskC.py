#! /usr/bin/env python
# Core imports
import time
import ev3dev.ev3 as ev3


def aroundObstacle():
    # connecting motors and sensors
    motorL =ev3.LargeMotor('outA')
    motorL.connected
    motorR =ev3.LargeMotor('outD')
    motorR.connected
    motorM =ev3.MediumMotor('outB')
    motorM.connected

    c = ev3.ColorSensor(ev3.INPUT_3)
    c.connected
    c.mode = 'COL-REFLECT'

    sonar = ev3.UltrasonicSensor(ev3.INPUT_4)
    sonar.connected
    sonar.mode = 'US-DIST-CM'

    # touch = ev3.TouchSensor(ev3.INPUT_1)
    # touch.connected



    # adaptation of TaskA followline_PID function
    def moving():
        # Constants for PID
        offset = 45
        Tp = 20
        Kp = 26

        # if(touch.is_pressed() == 1):
        #     ev3.Sound.speak('Exiting TaskC').wait
        #     time.sleep(3)

        # move forward until sonar detects object
        while(sonar.value() > 80 ):
           color = c.value()
           error = color - offset

           turn = Kp*error
           turn = turn/100
           powerL = Tp - turn
           powerR = Tp + turn

           motorR.run_timed(duty_cycle_sp = powerL, time_sp = 150)
           motorL.run_timed(duty_cycle_sp = powerR, time_sp = 150)
           time.sleep(.1)

        # then switch to circumvent function
        ev3.Sound.speak('Obstacle Detected').wait
        time.sleep(1)
        circumvent()

    # function to handles moving around obstacle
    def circumvent():
        # initial turn when obstacle is detected
        motorR.run_timed(duty_cycle_sp = 30, time_sp=3000)
        motorL.run_timed(duty_cycle_sp = -90, time_sp=3000)
        time.sleep(.2)
        motorM.run_timed(duty_cycle_sp = 30, time_sp=800)
        time.sleep(.2)

        # move forward for a bit as a buffer between turns
        motorL.run_timed(duty_cycle_sp=25, time_sp=800)
        motorR.run_timed(duty_cycle_sp=25, time_sp=800)
        time.sleep(.2)

        # PID constants
        offset = 90
        Tp = 30
        Kp = 12
        Ki = 0
        Kd = 0

        lastError = 0
        integral = 0
        colorVal = c.value()

        # if(touch.is_pressed() == 1):
        #     ev3.Sound.speak('Exiting TaskC').wait
        #     time.sleep(3)

        # while color sensor doesn't detect black line, go around obstacle
        # using PID controller proportional to ultrasonic value
        while (c.value() > 15):
            s = sonar.value()
            error = s - offset
            integral = integral + error
            derivative = error - lastError

            turn = Kp*error + Ki*integral + Kd*derivative
            turn = turn/1000
            powerL = Tp + turn
            powerR = Tp - turn

            motorL.run_timed(duty_cycle_sp = powerL, time_sp = 150)
            motorR.run_timed(duty_cycle_sp = powerR, time_sp = 150)
            lastError = error
            time.sleep(.1)

        # when color sensor detects black line, turn and follow line again
        ev3.Sound.speak('Found black line again').wait()
        motorR.run_timed(duty_cycle_sp = 60, time_sp=3000)
        motorL.run_timed(duty_cycle_sp = -60, time_sp=3000)
        time.sleep(.2)
        motorM.run_timed(duty_cycle_sp = -30, time_sp=800)
        time.sleep(.2)
        moving()

    # start with moving function
    moving()


aroundObstacle()
