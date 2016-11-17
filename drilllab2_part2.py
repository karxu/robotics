import time
import ev3dev.ev3 as ev3
import math
import utilities as util


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
