import time
import ev3dev.ev3 as ev3
import math
import utilities as util

def obstacleFinder():

    # define motors
    motorl =ev3.LargeMotor('outA')
    motorl.connected
    motorr =ev3.LargeMotor('outD')
    motorr.connected

    # define ultrasonic sensor
    sonar = ev3.UltrasonicSensor(ev3.INPUT_2)
    sonar.connected
    sonar.mode = 'US-DIST-CM',

    medmotor = ev3.MediumMotor('outB')
    medmotor.connected
    medmotor.reset
    # medmotor.position_sp = 50

    print("sonar value", sonar.value())
    print("medmotor position", medmotor.position)

    while True:
        print('boo')
        if (sonar.value() > 2000):
            medmotor.run_timed(duty_cycle_sp=25, time_sp=800)
            while 'running' in medmotor.state:
                print medmotor.state
            time.sleep(1)
            medmotor.run_timed(duty_cycle_sp=-25, time_sp=800)
            time.sleep(1)
        else:
            moveForward()
            break

    # while True:
    #     # if sonar does not detect anything less than 300mm away
    #     if (sonar.value() > 2400):
    #         # print current distance value in mm
    #         print(sonar.value()
    #         # move forward
    #         motorr.run_timed(duty_cycle_sp=25, time_sp=1000)
    #         motorl.run_timed(duty_cycle_sp=25, time_sp=1000)
    #     # else sonar does detect something less than 300mm away
    #     else if (sonar.value < 300)
    #     else:
    #         # print
    #         print("obstacle detected")
    #         # turn left
    #         motorr.run_timed(duty_cycle_sp=25, time_sp=2000)
    #         #break
    #         break

    print("done")
    time.sleep(1)


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
    motorl.run_timed(duty_cycle_sp=25, time_sp=4000)
    motorr.run_timed(duty_cycle_sp=25, time_sp=4000)

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
