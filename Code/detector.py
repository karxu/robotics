import time
import ev3dev.ev3 as ev3
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

        else:
            prev_val = sonar.value()

# "you will now exit the if/else statement and go back to the beg of the while loop"
