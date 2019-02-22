# importing the initialSetup
from initialSetup import *


# Some global constants/variables - all in the same place for easy changes
# The threshold distance for checking objects
scanDistance = 130.0

# The motors speed used in "goBack()" function. They are different because we
# want to go back, but also want to steer to right
goBackRightSpeed = 70
goBackLeftSpeed = 20

# The motors speed used in "takeItOut()" function
takeOutSpeed = 75

# The motors speed used in "searchForAnObject()" function
searchRightSpeed = 35
searchLeftSpeed = 35

# The pause times - used in time.sleep

# The recommended sleep time between ultrasonic sensor readings
# While working on the script we used this varible in multipple lines, but now
# it's only used in the "searchForAnObject()" function
pauseTime = 0.06
# Just a value chosen by us used in the while loop for the "takeItOut()"
# function
takeItOutPauseTime = 0.01 #


# Reading the measurements done by the ultrasonic sensor =
# = getting the distance in centimeters
def readUltrasonicSensor():

    GPIO.output(TRIGGER, True)
    time.sleep(0.001)
    GPIO.output(TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime

    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

# DESCRIPTION
# This function is used to check if the robocar did hit the black line or not.
# We decided to consider that the robocar got to the black line if any 2
# (out of 3) of our light sensors detect black, because during the development
# we've encountered different unsuitable situations:
#
# a) If we would consider that the robocar got to the black line only if 1
# sensor detects black, then we would get false interpretation [that we've hit
# the black line] because there were black spots on the board.
#
# b) If we would consider that the robocar got to the black line if all 3
# sensors detect black, then we would sometimes miss the black line completly
# because of the angle between the robocar trajectory and the black line.

# HOW IT WORKS
# The function starts by creating an empty list ("sensors") in which we append
# all 3 light sensors inputs using the global variables for pins from our
# "initialSetup" python file.
#
# Then we have an IF condition that checks if any 2 elements from the "sensors"
# list is equal to 1 (if any 2 (out of 3) of our light sensors detect black)
#
# If the condition is met then we return True.
# If the condition is not met then we return False.
def hitBlackLine():

    lightSensors = []
    lightSensors.append(GPIO.input(leftSensor))
    lightSensors.append(GPIO.input(middleSensor))
    lightSensors.append(GPIO.input(rightSensor))

    if lightSensors[0] == 1 and lightSensors[1] == 1 or \
    lightSensors[2] == 1 and lightSensors[1] == 1 or \
    lightSensors[0] == 1 and lightSensors[2] == 1:
        return True
    return False


# DESCRIPTION
# The "goBack()" function is used whenever we hit the black line so it's purpose
# was to make the robocar go back, but also to steer a little.
#
# Because we are spinning to right in our "searchForAnObject()" function we
# decided that in this case we will steer to right aswell.
#
# We want it to steer a little because after we push an object outside the
# perimeter, the robocar doesn't know it did that and it could get stuck into
# trying to push the same object and just going back, so after steering the
# robocar starts searching for a new object.

# HOW IT WORKS
# The function starts by making the robocar move backwards using the
# "backwards()" function from the "initialSetup" python file.
#
# Then the speed of the motors is set using the "goBackRightSpeed" and
# "goBackLeftSpeed" global variables.
#
# Then we have a time.sleep(0.8) statement because we want the robocar to move
# in the described manner for some time

def goBack():

    backwards()
    rightMotor.ChangeDutyCycle(goBackRightSpeed)
    leftMotor.ChangeDutyCycle(goBackLeftSpeed)
    time.sleep(0.8)

# DESCRIPTION
# The "takeItOut()" function is used to make the robocar move forward and push
# objects until it hits the black line.
#
# During the development, besides checking if it hit the black line, we also
# tried to check if there is still an object in front of the robocar while it's
# pushing it, but the accuracy of the sensor didn't helped (sometimes getting
# wrong readings), so we decided to drop this idea.
#
# The speed for the left motor is +3 because at high speeds (frequency = 50,
# duty cycle > 65) our robocar is steering a little to the left. We suspect this
# happens due to one of the left wheels sometimes touching the robocar chassis.
# This problem wasn't noticed while we did the line following script.

# HOW IT WORKS
# The function starts by making the robocar move forward using the "forward()"
# function from the "initialSetup" python file and the "takeOutSpeed" global
# variable.
#
# Then the function goes into a while loop and it checks if the robocar hits the
# black line using the "hitBlackLine()" function.
#
# If it didn't hit the black line (hitBlackLine() == False) we keep going
# forward at same speeds.
#
# Else (hitBlackLine() == True) we go back using the "goBack()" function and
# then we use a break statement to break out of the while loop.

def takeItOut():

    forward()
    rightMotor.ChangeDutyCycle(takeOutSpeed)
    leftMotor.ChangeDutyCycle(takeOutSpeed + 3)

    while True:
        if hitBlackLine() == False:
            time.sleep (takeItOutPauseTime)
        else:
            STOP()
            goBack()
            break

# DESCRIPTION
# The "searchForAnObject()" function is used to spin the robocar while searching
# for objects using the "readUltrasonicSensor()" function.
#
# We decided to spin to right because of
# the way the ultrasonic sensor works and how it was installed on our robocar
# The echo is on the right and the trigger is on the left, so the trigger
# follows the echo.
#
# During the development we tried different values for the motor speeds so we
# can find the balance between ultrasonic sensor accuracy and how fast our
# robocar is, but in the end we settled for 35

# HOW IT WORKS
# The function starts spinning to right by using the "turnRight()" function
# from the "initialSetup" python file. Then speed of the motors is set using the
# "searchRightSpeed" and "searchLeftSpeed" global variables.
#
# Then we have a while loop that gets the "distance" using the
# "readUltrasonicSensor()" function. The loop/function stops when we return True
# or False.
#
# If the "distance" is lower than the "scanDistance" global variable then we
# stop the robocar using the "STOP()" function from the "initialSetup" file and
# we return True.
#
# We also check if we encounter the black line while spinning using the
# "hitBlackLine()" function and if we do we stop the robocar using the "STOP()"
# function from the "initialSetup" file and we return False.
#
# The while loop ends with a time sleep statement using the pauseTime global
# variable

# OUTPUT:
# Returns "True" if it finds an object lower than the "scanDistance" global
# variable.
# Returns "False" if it gets to the black line.
def searchForAnObject():

    global scanDistance

    turnRight()
    rightMotor.ChangeDutyCycle(searchRightSpeed)
    leftMotor.ChangeDutyCycle(searchLeftSpeed)

    while True:
        distance = readUltrasonicSensor()
        if distance < scanDistance:

            STOP()
            return True

        if hitBlackLine() == True:

            STOP()
            return False

        time.sleep(pauseTime)

# DESCRIPTION
# In the "pushOutBoxes()" function we have the main while loop of this script.
#
# For testing purpose, we also use this function to check the running time for
# the whole script. We do that by by assigning the present time ("time.time()")
# to the "countTime" variable and we substruct this from the the present time
# ("time.time()") when the script gets to the "finally" clause.
#
# In this main loop we take actions based on the "searchForAnObject()" function
# output.
#
# This while loop is part of a try/except/finally statement. We are using this
# type of statement so we can have a way of stopping the script and also to
# perform some actions every time when that happens.
# The only handled exception is a "KeyboardInterrupt" exception (which pops when
# you stop the python script with the "CTRL+C" keyboard shortcut) for which a
# generic output is printed.
# The "finally" statement is used to stop the motors, to do a GPIO cleanup
# and also for printing the running time.

# HOW IT WORKS
# The function starts by assigning the present time ("time.time()") to the
# "countTime" variable.
#
# Then we have the "try" block and the "while" loop.
#
# Every time we loop we assign the output from the "searchForAnObject()"
# function to the "searchResult" variable.
#
# If the "searchResult" is "True" it means that an object was detected by the
# ultrasonic sensor and the distance from this object to our robocar is lower
# than the "scanDistance". In this case it means that we need to take out the
# object and we do that by calling the "takeItOut()" function.
#
# If the "searchResult" is "False" it means that we've hit the black line. In
# this case we have to avoid leaving the periemter and we do that by calling the
# "goBack()" function.
def pushOutBoxes():

    countTime = time.time()

    try:
        while True:

            searchResult = searchForAnObject()
            if searchResult == True:
                takeItOut()

            if searchResult == False:
                goBack()

    # Added this exception to get a certain output when we stop the script with
    # CTRL+C
    except KeyboardInterrupt:
        print ()
        print ("The script was stopped by keyboard")

    # We print the elapsed time, then we stop the motors and do a GPIO cleanup
    finally:
        print (time.time() - countTime)
        rightMotor.stop(0)
        leftMotor.stop(0)
        GPIO.cleanup()

# DESCRIPTION
# The main function

# HOW IT WORKS
# We call the necessary functions to start the motors and to push out the boxes
def main ():

    startMotors()
    pushOutBoxes()

# Calling the main() function
main()
