import time
import ev3dev.ev3 as ev3
import math
import utilities as util
import taskC as taskC

# declare sonar
sonar = ev3.UltrasonicSensor(ev3.INPUT_4)
sonar.connected
sonar.mode = 'US-DIST-CM'

# declare motors
motorL =ev3.LargeMotor('outA')
motorL.connected
motorR =ev3.LargeMotor('outD')
motorR.connected
motorM =ev3.MediumMotor('outB')
motorM.connected

# declare color sensor
c = ev3.ColorSensor(ev3.INPUT_3)
c.connected
c.mode = 'COL-REFLECT'

###########################################################
#################### Main Functions #######################
###########################################################

# "include if statement in the followLine code that calls the circumvent() function"
# "when the sonar.value() < 150"

def circumvent():

    prev_val = 0;       # keeps track of previous sonar value
    diff = 0;           # keeps track of diff btwn current val and prev val

    turnL()             # robot will always turn left first
    time.sleep(1)

    while True:

# "include an if statement that allows robot to exit the circumvent() function when"
# "it detects the line from the color sensor"
        if ( c.value() < 40 ): # you may need to change the integer
            taskC.followLine()
            break

        # ev3.Sound.speak('Going straight').wait()
        moveForward()   # note: the new current val is now sonar.value()

        # calculate difference
        diff = sonar.value() - prev_val
        print("Diff: " + str(diff))

        # if the diff > 290, that means you reached the edge of the obstacle
        # ie. WALL = 30, NO WALL = 900, DIFF = 870
        if( (abs(diff) > 290) ):
            turnR()
            prev_val = sonar.value()

        # if the diff < 290, that means you did not reach the edge
        # ie. WALL = 30, WALL CONTINUED = 35, DIFF = 5
        else:
            prev_val = sonar.value()

# "you will now exit the if/else statement and go back to the beg of the while loop"

###########################################################
#################### Test Functions #######################
###########################################################

# this is pretty useless **ignore for now**
# def testAvoidObstacle():
#     while True:
#
#         if( sonar.value() < 150 ):
#             ev3.Sound.speak('help me').wait()
#
#             turnL()
#             print(str(sonar.value()))
#             time.sleep(3)
#
#             while ( sonar.value() < 700 ):
#                 moveForward()
#
#             val1 = sonar.value()
#             print(str(val1))
#             time.sleep(3)
#
#             turnR()
#             val2 = sonar.value()
#             print(str(val2))
#             time.sleep(3)
#
#             change = val1-val2
#
#             if(change>400):
#                 while ( sonar.value() < 1000 ):
#                     moveForward()
#
#             turnR()
#             print("done")
#             time.sleep(1)
#
#             break
#         else:
#             moveForward()

# use this to print sonar values at 3 sec intervals + store them in a .txt file
def testSonar():

    btn = ev3.Button()

    readings = ""
    readings_file = open('sonar_results.txt', 'w')

    while not btn.backspace:
        readings = readings + str(sonar.value()) + '\n'
        print(str(sonar.value()))
        time.sleep(3)
    readings_file.write(readings)
    readings_file.close()

###########################################################
################## Helper Functions #######################
###########################################################

# when turning right, motorR moves slightly as well so it can turn wider
def turnR():
    ev3.Sound.speak('Turning right').wait()
    print("turn right")
    motorL.run_timed(duty_cycle_sp = 50, time_sp=2000)
    motorR.run_timed(duty_cycle_sp = 10, time_sp=2000)
    time.sleep(.2)

    time.sleep(.2)

# when turning left, the eyes also turn so the robot can keep track of the wall
def turnL():
    print("turn left")
    motorR.run_timed(duty_cycle_sp = 27, time_sp=2000)
    motorM.run_timed(duty_cycle_sp = 45, time_sp=300)
    time.sleep(.2)

# moves forward
def moveForward():
    motorL.run_timed(duty_cycle_sp=25, time_sp=800)
    motorR.run_timed(duty_cycle_sp=25, time_sp=800)
    time.sleep(0.5)


    # Onji's brute force logic copied over from TaskC
    # prev_val = 0;       # keeps track of previous sonar value
    # diff = 0;           # keeps track of diff btwn current val and prev val
    # while (colorVal > 15):
    #     # calculate difference
    #     moveForward()
    #     diff = sonar.value() - prev_val
    #     print("Diff: " + str(diff))
    #     # if the diff > 290, that means you reached the edge of the obstacle
    #     # ie. WALL = 30, NO WALL = 900, DIFF = 870
    #     if( (abs(diff) > 290) ):
    #         ev3.Sound.speak('Turning right').wait()
    #         turnR()
    #         time.sleep(1)
    #         prev_val = sonar.value()
    #         colorVal = c.value()
    #     else:
    #         prev_val = sonar.value()
    #         colorVal = c.value()
