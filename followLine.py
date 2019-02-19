# importing the initialSetup
from initialSetup import *
# To get the PID.Value we used another python script which we import here.
import PID

# This script was designed to control a robocar in order for it to follow a
# black line, using 3 light sensors.
#
# It is based on a PID (proportional–integral–derivative) controller algorithm.
# The algorithm implementation is in the "PID.py" file
#
#
# The "followLine()" function we have the main while loop of this script.
#
# This while loop is part of a try/except/finally statement. We are using this
# type of statement so we can have a way of stopping the script and also to
# perform some actions every time when that happens.
# The only handled exception is a "KeyboardInterrupt" exception (which pops when
# you stop the python script with the "CTRL+C" keyboard shortcut) for which a
# generic output is printed.
# The "finally" statement is used to stop the motors, to do a GPIO cleanup
# and also for printing the running time.
#
# At the begging of our while loop we create an empty list ("sensors") in which
# we append all 3 light sensors using the global variables for pins from our
# "initialSetup" python file ("leftSensor", "middleSensor", "rightSensor").
#
# Then we calculate the error using the "calculateError()" function from the
# "PID.py" file and based on that we calculate the measured process variable
# (PV)-- which is called "PID.value" in our scripts - using the "calculatePID()"
# function
#
# We use an "initialSpeed" variable from which we add or substruct the PID.Value,
# based on the direction the car needs to go.
#
# We always multiply the speeds by 0.9
# because we saw that the motors start acting strangely if the duty cycle is bigger
# than 90. When we go forward, we don't use the PID value, but just a KS variable
# that we've come up with and the "initialSpeed". We do this because we want the
# car to go faster when it is centered on the black line
#
# At the end of our while loop we sleep for a little time - time.sleep (0.01)
#
# The "initialSpeed", "KS", "KP" have some certain specific values. We came up with
# this values after a lot of trial and error test with our robocar.

def followLine():
    writeRunScriptFile = open("/var/www/html/runFollowLineScript", 'w')
    writeRunScriptFile.write("0")
    writeRunScriptFile.close()

    startMotors()
    stopScriptCounter = 0

    try:
        while True:

            # The next code checks if the user wants to stop this script from the web interface
            stopScriptCounter += 1
            if stopScriptCounter == 50:
                stopFollowLineFile = open("/var/www/html/stopFollowLine", 'r')
                stopScript = int(stopFollowLineFile.read())
                stopFollowLineFile.close()
                if stopScript == 0:
                    print ("S-a oprit!")
                    break
                stopScriptCounter = 0

            # Adding the sensor readings to a list

            sensors = []
            sensors.append(GPIO.input(leftSensor))
            sensors.append(GPIO.input(middleSensor))
            sensors.append(GPIO.input(rightSensor)

            # Calculating the PID error based on the sensors list
            PID.calculateError(sensors)
            PID.calculatePID()

            initialSpeed = 49
            KS = 1.6

            if PID.direction == "right":
                speed = PID.PIDvalue
                if (initialSpeed - speed < 0):

                    rightSpeed = abs(initialSpeed - speed) * 0.9
                    leftSpeed = (initialSpeed + speed) * 0.9
                    rightMotor.ChangeDutyCycle(rightSpeed)
                    leftMotor.ChangeDutyCycle(leftSpeed)
                    turnRight()

                else:

                    rightSpeed = (initialSpeed - speed) * 0.9
                    leftSpeed = (initialSpeed + speed) * 0.9
                    rightMotor.ChangeDutyCycle(rightSpeed)
                    leftMotor.ChangeDutyCycle(leftSpeed)
                    forward()

            elif PID.direction == "forward":

                speed = initialSpeed * KS
                rightSpeed = speed * 0.9
                leftSpeed = speed * 0.9
                rightMotor.ChangeDutyCycle(rightSpeed)
                leftMotor.ChangeDutyCycle(leftSpeed)
                forward()

            elif PID.direction == "left":
                speed = PID.PIDvalue
                if (initialSpeed + speed < 0):

                    rightSpeed = (initialSpeed - speed) * 0.9
                    leftSpeed = abs(initialSpeed + speed) * 0.9
                    rightMotor.ChangeDutyCycle(rightSpeed)
                    leftMotor.ChangeDutyCycle(leftSpeed)
                    turnLeft()

                else:

                    rightSpeed = (initialSpeed - speed) * 0.9
                    leftSpeed = (initialSpeed + speed) * 0.9
                    rightMotor.ChangeDutyCycle(rightSpeed)
                    leftMotor.ChangeDutyCycle(leftSpeed)
                    forward()

            time.sleep (0.01)

    except KeyboardInterrupt:
        print ()
        print ("Follow the line script was interrupted from keyboard")

    finally:
        writeRunScriptFile = open("/var/www/html/runFollowLineScript", 'w')
        writeRunScriptFile.write("1")
        writeRunScriptFile.close()

        stopFollowLineFile = open("/var/www/html/stopFollowLine", 'w')
        stopFollowLineFile.write("1")
        stopFollowLineFile.close()

        GPIO.cleanup()

# The main function
# This script uses the same logic as the movemnt script regarding the
# running and stoping from the web interface
def main():
    readRunScriptFile = open("/var/www/html/runFollowLineScript", 'r')
    runScript = readRunScriptFile.readline().rstrip()
    readRunScriptFile.close()

    if runScript == "1":
        followLine()

# Calling the main function
main()
