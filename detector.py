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
    sonar = ev3.UltrasonicSensor(ev3.INPUT_1)
    sonar.connected
    sonar.mode = 'US-DIST-CM'

    while True:
        # if sonar does not detect anything less than 300mm away
        if (sonar.value() > 300):
            # print current distance value in mm
            print(str(sonar.value()))
            # move forward
            motorr.run_timed(duty_cycle_sp=25, time_sp=1000)
            motorl.run_timed(duty_cycle_sp=25, time_sp=1000)
        # else sonar does detect something less than 300mm away
        else:
            # print
            print("obstacle detected")
            # turn left
            motorr.run_timed(duty_cycle_sp=25, time_sp=2000)
            #break
            break

    print("done")
    time.sleep(5)

def operateWheelsBasic():
    print "spin the wheels"

# # left wheel is attached to outA
# # right wheel is attached to outD

    # motor encoder
    # initial_pos = motorl.position
    # print('initial position: %d', initial_pos)

    # readings = ""
    # readings_file = open('drill2.txt', 'w')
    # readings = str(initial_pos) + '\n'
    # readings_file.write(readings)
    # readings_file.close()

    # run_time takes milliseconds
    motorl.run_timed(duty_cycle_sp=25, time_sp=2000)
    motorr.run_timed(duty_cycle_sp=25, time_sp=2000)

    final_pos = motorl.position

    readings = ""
    readings_file = open('drill2.txt', 'w')
    readings = str(final_pos) + '\n'
    readings_file.write(readings)
    readings_file.close()

    time.sleep(5)
    # why do we need this line above in order to get the motor to run????????
