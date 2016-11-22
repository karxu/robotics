import ev3dev.ev3 as ev3
import time
import utilities as util

import taskA_PID as taskA


motorl = ev3.LargeMotor('outA')
motorl.connected
motorr = ev3.LargeMotor('outD')
motorr.connected
c = ev3.ColorSensor(ev3.INPUT_3)
c.connected
c.mode = 'COL-REFLECT'

def calculating_pid():  #possibly rename?
    # taskA.calibrate()
    black = 6             #how to get value
    white = 80             #how to get value
    Tp = 30
    offset = (white + black)/2
    Kp = (0 - Tp)/((black - offset) - 0)    #fine tune through experimentation
    Kp = Kp * 100        #to help with integer math restrictions comment on test to see if makes difference
    Ki = 100 #1x100       #Ki requires finetuning through trial and error
    Kd = 10000  #needs trial and error finetuning. hard code?
    #test values
    integral = 0
    last_error = 0     #initialising
    derivative = 0     #initialising
    t = 1     #Change value to while motor is runnig
    while (t==1):
        colour = c.value()         #how to get value (light reading)
        error = colour - offset
        integral = integral + error
        derivative = error - last_error
        turn = Kp*error + Ki*integral + Kd*derivative
        turn = turn/100   #comment out with kp*100 in test to see if makes difference
        powerleft = Tp + turn
        powerright = Tp - turn
        if powerleft > 0:
           motorl.run_direct(duty_cycle_sp = powerleft)
        else:
           powerleft = powerleft * (-1)
           motorl.run_direct(duty_cycle_sp = powerleft)
        if powerright < 0:
           motorr.run_direct(duty_cycle_sp = powerright)
        else:
           powerright = powerright * (-1)
           motorr.run_direct(duty_cycle_sp = powerright)
        last_error = error
		#possibly include catch for motor speeds greater than 100
