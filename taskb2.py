import ev3dev.ev3 as ev3
import time

motorl = ev3.LargeMotor('outA')
motorl.connected
motorr = ev3.LargeMotor('outD')
motorr.connected
c = ev3.ColorSensor(ev3.INPUT_3)
c.connected
c.mode = 'COL-REFLECT'

def runningw():
    integral = 0
    offset = 45
    last_error = 0
    Tp = 24
    Kp = 26
    Kp = Kp * 100        #to help with integer math restrictions comment on test to see if makes difference
    Ki = 0                #1x100       #Ki requires finetuning through trial and error
    Kd = 0
    while c.value() < 40:
        colour = c.value()         #how to get value (light reading)
        error = colour - offset
        integral = integral + error
        derivative = error - last_error
        turn = Kp*error + Ki*integral + Kd*derivative
        turn = turn/100   #comment out with kp*100 in test to see if makes difference
        powerleft = Tp + turn
        powerright = Tp - turn
        # while powerleft > 0:
        motorl.run_direct(duty_cycle_sp = powerleft)
        # else:
            # powerleft = powerleft * (-1)
            # while powerleft > 0:
                # motorl.run_direct(duty_cycle_sp = powerleft)
        # while powerright < 0:
        motorr.run_direct(duty_cycle_sp = powerright)
        # else:
            # powerright = powerright * (-1)
            # while powerright < 0:
                # motorr.run_direct(duty_cycle_sp = powerright)
        time.sleep(.1)
        last_error = error

def runningb():
    colour = c.value()
    integral = 0
    offset = 45
    last_error = 0
    Tp = 24
    Kp = 26
    Kp = Kp * 100        #to help with integer math restrictions comment on test to see if makes difference
    Ki = 0            #1x100       #Ki requires finetuning through trial and error
    Kd = 0                 #needs trial and error finetuning. hard code?
    while(color > 15):
        colour = c.value()         #how to get value (light reading)
        error = colour - offset
        integral = integral + error
        derivative = error - last_error
        turn = Kp*error + Ki*integral + Kd*derivative
        turn = turn/100   #comment out with kp*100 in test to see if makes difference
        powerleft = Tp + turn
        powerright = Tp - turn
        # while powerleft > 0:
        motorl.run_direct(duty_cycle_sp = powerleft)
        # else:
        #     powerleft = powerleft * (-1)
        #     while powerleft > 0:
        #         motorl.run_direct(duty_cycle_sp = powerleft)
        # while powerright < 0:
        motorr.run_direct(duty_cycle_sp = powerright)
        # else:
        #     powerright = powerright * (-1)
        #     while powerright < 0:
        #         motorr.run_direct(duty_cycle_sp = powerright)
        time.sleep(.1)
        last_error = error

def taskB():
    side = 1
    line = 0
    while line < 3:
        runningw()
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
       motorl.run_timed(duty_cycle_sp = 70, time_sp=500)   #experimented with hard value here, 10:-20. 30:-20, 30:0, (too small) 100|:0, 100:-50, (overshooting) 90:-30(best), 45:0, 50:0, 70:0, 80,0, 70:-10
       motorr.run_timed(duty_cycle_sp = -5, time_sp=500)  #and the time stamp 100 1000 10000 500(best time)
       time.sleep(1)
       runningb()
       motorl.run_timed(duty_cycle_sp = -5, time_sp=500)
       motorr.run_timed(duty_cycle_sp = 70, time_sp=500)
       time.sleep(1)
    else:
    #    ev3.Sound.speak('I have reached the end of the line and will search on the left for the next line').wait()
       motorl.run_timed(duty_cycle_sp = -5, time_sp=500)
       motorr.run_timed(duty_cycle_sp = 70, time_sp=500)
       time.sleep(1)
       runningb()
       motorl.run_timed(duty_cycle_sp = 70, time_sp=500)
       motorr.run_timed(duty_cycle_sp = -5, time_sp=500)
       time.sleep(1)
    return


taskB()
