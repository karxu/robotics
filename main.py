#! /usr/bin/env python
# Core imports
import time
import ev3dev.ev3 as ev3

# Local Imports
import tutorial as tutorial
import utilities
import openLoopControl as olc
import detector as detector
import taskA as taskA
import taskA_PID as taskA_PID
import taskB as taskB

# print ('hello')

ev3.Sound.speak('hello').wait()

# Step A: Basic open driving
# tutorial.operateWheelsBasic()

# Step B: Turn on an off an LED using a switch
# tutorial.makeLightSwitch()

# Step C: Use switches to drive robot back and forward
# tutorial.makeLightAndMotorSwitch()

# Step D: Use a class to develop a bigger program with a state
# o = olc.openLoopControl()
# # execute (with default params)
# o.operateWheels()
# # update parameters
# o.time_to_spin = 1.0
# o.duty_cycle_sp = 50
# # execute again
# o.operateWheels()

# Step E: Record values from the ultrasonic to a text file
# tutorial.recordUltraSonic()

# detector.moveForward()
# detector.obstacleFinder()
# detector.gyroReading()
# taskA.followline()
# taskA_PID.calibrate()
taskA_PID.followline_PID()
# detector.circumvent()
# detector.testSonar()
# detector.turnL()

# remove this if you want it to exit as soon as its done:
# wasn't working until I added parenthesis (Wed, 16, 3:40)
print("main: wait 2sec, then end")
time.sleep(2)
