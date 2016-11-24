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

def taskB():
    side = 1
    line = 0
    powerleft = 20
    powerright = 20
    while line < 3:
        while (c.value() <= 20):
            motorl.run_direct(duty_cycle_sp = powerleft)
            motorr.run_direct(duty_cycle_sp = powerright)
            time.sleep(.1)
            print(c.value())
        motorl.run_direct(duty_cycle_sp = 0)
        motorr.run_direct(duty_cycle_sp = 0)
        time.sleep(1)
        turn(side)
        side = side + 1
        line = line + 1
    motorl.run_timed(duty_cycle_sp = 30, time_sp=30000)
    motorr.run_timed(duty_cycle_sp = 30, time_sp=30000)


def turn(side):
    #even numbers left inside line, odd numbers right inside line
    if (side%2 == 0):
    #    ev3.Sound.speak('I have reached the end of the line and will search on the right for the next line').wait()
       #turn 90 degrees
       motorl.run_timed(duty_cycle_sp = 77, time_sp=550)   #experimented with hard value here, 10:-20. 30:-20, 30:0, (too small) 100|:0, 100:-50, (overshooting) 90:-30(best), 45:0, 50:0, 70:0, 80,0, 70:-10
       motorr.run_timed(duty_cycle_sp = -10, time_sp=550)  #and the time stamp 100 1000 10000 500(best time)
       time.sleep(1)
       detectnewline()
       motorl.run_timed(duty_cycle_sp = -10, time_sp=550)
       motorr.run_timed(duty_cycle_sp = 80, time_sp=550)
       time.sleep(1)
    else:
    #    ev3.Sound.speak('I have reached the end of the line and will search on the left for the next line').wait()
       motorl.run_timed(duty_cycle_sp = -10, time_sp=550)
       motorr.run_timed(duty_cycle_sp = 77, time_sp=550)
       time.sleep(1)
       detectnewline()
       motorl.run_timed(duty_cycle_sp = 80, time_sp=550)
       motorr.run_timed(duty_cycle_sp = -10, time_sp=550)
       time.sleep(1)
    return

def detectnewline():
    powerleft = 20
    powerright = 20
    while (c.value() > 20):
        print(c.value())
        motorl.run_direct(duty_cycle_sp = powerleft)
        motorr.run_direct(duty_cycle_sp = powerright)
        time.sleep(.1)
    motorl.run_timed(duty_cycle_sp = -1, time_sp=5)
    motorr.run_timed(duty_cycle_sp = -1, time_sp=5)
    time.sleep(1)
    return


taskB()

# def taskB():
#     motorl.run_timed(duty_cycle_sp = 70, time_sp=500)   #experimented with hard value here, 10:-20. 30:-20, 30:0, (too small) 100|:0, 100:-50, (overshooting) 90:-30(best), 45:0, 50:0, 70:0, 80,0, 70:-10
#     motorr.run_timed(duty_cycle_sp = -10, time_sp=500)   #and the time stamp 100 1000 10000 500(best time)
#
#
# taskB()
