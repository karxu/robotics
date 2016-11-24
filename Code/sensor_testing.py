import time
import ev3dev.ev3 as ev3
import math
import utilities as util


def color_calibrate():
    c = ev3.ColorSensor(ev3.INPUT_3)
    c.connected
    c.mode = 'COL-REFLECT'

    ev3.Sound.speak('Place robot on white').wait()
    print('Place on white')
    time.sleep(3)
    white1 = c.value()
    print(white1)
    ev3.Sound.speak('Place robot on another white').wait()
    print('Place on another white')
    time.sleep(3)
    white2 = c.value()
    print(white2)


    ev3.Sound.speak('Place robot on black').wait()
    print('Place on black')
    time.sleep(3)
    black1 = c.value()
    print(black1)
    ev3.Sound.speak('Place robot on another black').wait()
    print('Place on another black')
    time.sleep(3)
    black2 = c.value()
    print(black2)

    offset = (white1 + white2 + black1 + black2)/4
    print('OFFSET' + str(offset))
    time.sleep(10)



def sonarTesting():
    # declare sonar
    sonar = ev3.UltrasonicSensor(ev3.INPUT_4)
    sonar.connected
    sonar.mode = 'US-DIST-CM'
    motorM =ev3.MediumMotor('outB')
    motorM.connected

    ev3.Sound.speak('Place robot at obstacle start').wait()
    print('Place at obstacle start')
    sonar1 = sonar.value()
    print(sonar1)
    motorM.run_timed(duty_cycle_sp = 45, time_sp=400)
    time.sleep(1)

    ev3.Sound.speak('start moving').wait()
    print('start moving')
    time.sleep(1)
    counter = 0
    while(counter < 20):
        sonar2 = sonar.value()
        print(sonar2)
        time.sleep(1)
        counter += 1
    ev3.Sound.speak('finished').wait()

def motorTesting():
    # connecting motors
    motorL =ev3.LargeMotor('outA')
    motorL.connected
    motorR =ev3.LargeMotor('outD')
    motorR.connected
    motorM =ev3.MediumMotor('outB')
    motorM.connected
    print("turn left")
    motorR.run_timed(duty_cycle_sp = 10, time_sp=3000)
    motorL.run_timed(duty_cycle_sp = -90, time_sp=3000)
    time.sleep(.2)
    motorM.run_timed(duty_cycle_sp = 60, time_sp=800)
    time.sleep(.2)

def turnL():
    motorL =ev3.LargeMotor('outA')
    motorL.connected

    motorM =ev3.MediumMotor('outB')
    motorM.connected

    print("turn left")
    motorL.run_timed(duty_cycle_sp = -80, time_sp=3000)
    time.sleep(.2)
    motorM.run_timed(duty_cycle_sp = 58, time_sp=1000)
    time.sleep(.2)
