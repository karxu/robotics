#! /usr/bin/env python
# Core imports
import time
import ev3dev.ev3 as ev3

# Local Imports
import detector as detector
import taskA as taskA
import taskB as taskB
import taskC as taskC
import sensor_testing as testing

ev3.Sound.speak('hello there, I hope this demo goes well').wait()

touch = ev3.TouchSensor()
touch.connected


counter = 0

if(touch.is_pressed() == True):
    counter += 1
    print('counter', counter)

if(counter == 1):
    ev3.Sound.speak('starting task A').wait()
    time.sleep(1)
    taskA.followline_PID()

if(counter == 2):
    ev3.Sound.speak('starting task B').wait()
    time.sleep(1)
    taskB.taskB()

if(counter == 3):
    ev3.Sound.speak('starting task C').wait()
    time.sleep(1)
    taskC.aroundObstacle()

# i didn't actually put in a stop for C, because i realized you can't do that from
# this main file, unless you think of another way

# we'll have to rerun main.py between the tasks but we don't have to reconnect
# it to a computer this way


time.sleep(5)
