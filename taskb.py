import ev3dev.ev3 as ev3
import time

motorl = ev3.LargeMotor('outA')
motorl.connected
motorr = ev3.LargeMotor('outD')
motorr.connected
c = ev3.ColorSensor(ev3.INPUT_3)
c.connected
c.mode = 'COL-REFLECT'


#insert PID here
powerleft = 30
powerright = 30

def taskB():
    side = 1
    line = 0
    while line < 3:
        if (colour > 15):
            forward()
        else:
            motorl.run_direct(duty_cycle_sp = 0)
            motorr.run_direct(duty_cycle_sp = 0)
            time.sleep(.2)
            turn()
        line = line + 1
    motorl.run_timed(duty_cycle_sp = 30, time_sp=3000)
    motorr.run_timed(duty_cycle_sp = 30, time_sp=3000)

def forward():
    motorl.run_direct(duty_cycle_sp = powerleft)
    motorr.run_direct(duty_cycle_sp = powerright)
    time.sleep(.2)

def turn():
    #even numbers left inside line, odd numbers right inside line
    if (side%2 == 0):
       ev3.Sound.speak('I have reached the end of the line and will search on the right for the next line').wait()
       #turn 90 degrees
       motorl.run_timed(duty_cycle_sp = 30, time_sp=1000)
       motorr.run_timed(duty_cycle_sp = -30, time_sp=1000)
       time.sleep(.2)
       detectnewline()
       motorl.run_timed(duty_cycle_sp = -30, time_sp=1000)
       motorr.run_timed(duty_cycle_sp = 30, time_sp=1000)
       time.sleep(.2)
    else:
       ev3.Sound.speak('I have reached the end of the line and will search on the left for the next line').wait()
       motorl.run_timed(duty_cycle_sp = -30, time_sp=1000)
       motorr.run_timed(duty_cycle_sp = 30, time_sp=1000)
       time.sleep(.2)
       detectnewline()
       motorl.run_timed(duty_cycle_sp = 30, time_sp=1000)
       motorr.run_timed(duty_cycle_sp = -30, time_sp=1000)
       time.sleep(.2)
    side = side + 1

def detectnewline():
    while (colour < 15):
        forward()
