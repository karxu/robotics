#! /usr/bin/env python
# Core imports
import time
import ev3dev.ev3 as ev3

# Local Imports
import sensor_testing as sensor_testing
import taskA as taskA
import taskB as taskB
import taskC as taskC
import detector as detector

#testing
# sensor_testing.color_calibrate()
# sensor_testing.sonarTesting()
# sensor_testing.motorTesting()
# sensor_testing.turnL()

# Task A
# taskA.followline()
taskA.followline_PID()
time.sleep(10)

# Task B
taskB.taskB()
time.sleep(10)

# Task C
# detector.circumvent()
taskC.aroundObstacle()
time.sleep(10)
