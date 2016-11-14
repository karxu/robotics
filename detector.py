import time
import ev3dev.ev3 as ev3
import math

def operateWheelsBasic():
    print "spin the wheels"

# left wheel is attached to outA
# right wheel is attached to outD

    motorl =ev3.LargeMotor('outA')
    motorl.connected

    motorr =ev3.LargeMotor('outD')
    motorr.connected

    # run_time takes milliseconds
    motorl.run_timed(duty_cycle_sp=20, time_sp=2000)
    motorr.run_timed(duty_cycle_sp=20, time_sp=2000)
    time.sleep(1)
    # motor.run_timed(duty_cycle_sp=-25, time_sp=500)

    print('sleeping for 1 second')
    time.sleep(1)
