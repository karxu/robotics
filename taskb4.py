import ev3dev.ev3 as ev3
import time

motorl = ev3.LargeMotor('outA')
motorl.connected
motorr = ev3.LargeMotor('outD')
motorr.connected
c = ev3.ColorSensor(ev3.INPUT_3)
c.connected
c.mode = 'COL-REFLECT'
colour = c.value()

x = 475
y = 85
z = -5

def taskB():
    side = 1   #which side the robot begins from
    line = 0   #the lines the robot has advanced on
    while line < 4: #while having not reached the end of the track continue advancing
        while c.value() < 80:   #having not reached the end of the line/detected white move forward
            forward(side)
        motorl.run_direct(duty_cycle_sp = 0)
        motorr.run_direct(duty_cycle_sp = 0)
        time.sleep(1)
        turn(side)
        side = side + 1
        line = line + 1
    motorl.run_timed(duty_cycle_sp = 30, time_sp=2000)
    motorr.run_timed(duty_cycle_sp = 30, time_sp=2000)

def turn(side):
    x = 475  #variables for determing power output
    y = 85
    z = -5
    if (side%2 == 0): #even numbers left inside line, odd numbers right inside line
       ev3.Sound.speak('I have reached the end of the line and will search on the right for the next line').wait()
       #turn 90 degrees left
       #proceed forward until reach next line
       #turn 90 degrees right to position for next advancement
       motorl.run_timed(duty_cycle_sp = y, time_sp = x)   #experimented with hard value here, 10:-20. 30:-20, 30:0, (too small) 100|:0, 100:-50, (overshooting) 90:-30(best), 45:0, 50:0, 70:0, 80,0, 70:-10
       motorr.run_timed(duty_cycle_sp = z, time_sp = x)  #and the time stamp 100 1000 10000 500(best time)
       time.sleep(.1)
       detectnewline()
       motorl.run_timed(duty_cycle_sp = z, time_sp = x)
       motorr.run_timed(duty_cycle_sp = y, time_sp = x)
       time.sleep(.1)
    else:
       #90 degrees right
       #then 90 degrees left
       ev3.Sound.speak('I have reached the end of the line and will search on the left for the next line').wait()
       motorl.run_timed(duty_cycle_sp = z, time_sp = x)
       motorr.run_timed(duty_cycle_sp = y, time_sp = x)
       time.sleep(.1)
       detectnewline()
       motorl.run_timed(duty_cycle_sp = y, time_sp = x)
       motorr.run_timed(duty_cycle_sp = z, time_sp = x)
       time.sleep(.1)
    return

def detectnewline():
    powerleft = 20
    powerright = 20
    while (c.value() > 20): #proceed forward until next line (black) detected
        print(c.value())
        motorl.run_direct(duty_cycle_sp = powerleft)
        motorr.run_direct(duty_cycle_sp = powerright)
        time.sleep(.1)
    motorl.run_timed(duty_cycle_sp = -3, time_sp=10)
    motorr.run_timed(duty_cycle_sp = -3, time_sp=10)
    time.sleep(1)
    return

def forward(side):
    #move forward under PID  controller following edge of line
    offset = 45
    Tp = 20
    Kp = 26
    while(c.value() < 80):
         colour = c.value()
         error = colour - offset
         turn = Kp*error
         turn = turn/100
         if (side%2 == 0):
              powerl = Tp - turn
              powerr = Tp + turn
         else:
             powerl = Tp + turn
             powerr = Tp - turn
         motorl.run_direct(duty_cycle_sp = powerl)
         motorr.run_direct(duty_cycle_sp = powerr)
         motorl.run_timed(duty_cycle_sp = -3, time_sp=10)
         motorr.run_timed(duty_cycle_sp = -3, time_sp=10)
         time.sleep(.1)

taskB()
