# TO DO:
# 1. Be sure to check if you hit the black line every fucking time you move that car - EVERYFUCKINGTIME
# 2. Deal with the hitBlackLine() - If your car is on the line be sure to move in the opposite direction
# 3. Check the maxmium distance of the perimeter
# 4. Maybe do the 360 degree thing?

### QUESIONS FOR THE TECHERS REGARDINg THE RULES:
# 1. Define when an object is excluded from the perimeter
# - do we have to move the majority of the object outside of our perimter (center of graivty/mass)?
# - does the object has to be
# 2. After the object has been pushed from the perimeter, can we physically move it from the side of
#   the perimeter or do we have to leave it there?


#import libraries
from initialSetup import *
from hcsr04sensor import sensor
from PID import printSensors

scanDistance = 85
pauseTime = 0.01

# In this function we check if we've hit the black line or not
def hitBlackLine():

    sensors = []
    sensors.append(GPIO.input(leftSensor))
    sensors.append(GPIO.input(middleSensor))
    sensors.append(GPIO.input(rightSensor))

    if sensors[0] == 1 and sensors[1] == 1 and sensors[2] == 1:
        # \
    # and sensors[1] == 1 or \
    #sensors[0] == 1 and sensors[2] == 1:
        return True

    return False
# Reading the measurements done by the ultrasonic sensor = getting the distance
# Be sure to check the time.sleep options
def readUltrasonicSensor():

    trig_pin = 40
    echo_pin = 38
    # Default values
    # unit = 'metric'
    # temperature = 20
    # round_to = 1

    # Create a distance reading with the hcsr04 sensor module
    # using GPIO.BOARD pin values.
    value = sensor.Measurement(trig_pin, echo_pin, gpio_mode=GPIO.BOARD)
    distance = value.raw_distance()


    #print (raw_measurement)

    return distance



# Taking an timeGiven argument and sleeping through it all in small pieces
def timeSleepAndCheckIfHitBlackLine (t):

    oo1 = 0.01
    timeGiven = t
    print ("Sleeping and checking for black line")
    while timeGiven > 0.0:

        timeGiven -= oo1
        if hitBlackLine() == True:
            return True
        time.sleep(oo1)

    return False



def timeSleepAndCheckIfFoundAnyObject(t):

    aTime = time.time()
    global scanDistance

    timeGiven = t
    oo1 = 0.01
    print ("Sleeping and checking for object")

    while timeGiven > 0.0:

        timeGiven -= ooo1
        distance = readUltrasonicSensor()
        if int(distance) < scanDistance:
            STOP()
            print ("time: ", time.time() - aTime)
            return True
        time.sleep(ooo1)

    print ("time: ", time.time() - aTime)
    return False



def rightCurve (localTime):
    turnRight()
    rightMotor.ChangeDutyCycle(35)
    leftMotor.ChangeDutyCycle(35)
    time.sleep(localTime)

def leftCurve (localTime):
    turnLeft()
    rightMotor.ChangeDutyCycle(35)
    leftMotor.ChangeDutyCycle(35)
    time.sleep(localTime)






# This function comes into action when we hit the black line
# How it works:
# 1. First it goes back for 1 second at speed 30
# 2. Then it turns a little and it also checks (while it's turning) if we get a posive reading
def goBack():
    print("Going back !!")
    rightMotor.ChangeDutyCycle(55)
    leftMotor.ChangeDutyCycle(25)
    backwards()
    time.sleep(1)

    #distance = readUltrasonicSensor()
    #rightCurve(0.3)

    #if timeSleepAndCheckIfFoundAnyObject(0.2) == True:
    #        takeItOut()

    print ("######################### END goBack()")







# This function is used when we have a positive reading (object in front and at a good distance) and
# we just want to take that object out of the perimeter
# How it works:
# 1. First it takes a little breath by stoping the car
# 2. Then it checks if it hits the black line in the current positions and if it
# does so, the whole function stops (return), else it goes forward for a little
# and it does another reading of the distance
# 3. The it goes into a while loop that keeps verifying if we get a positive
# reading and if we do we move forward
def takeItOut():

    reading = 0
    takeOutSpeed = 50

    # 1.
    print ("Taking it out!")
    STOP()
    time.sleep(0.1)

    # 2.
    forward()
    rightMotor.ChangeDutyCycle(takeOutSpeed)
    leftMotor.ChangeDutyCycle(takeOutSpeed)
    distance = readUltrasonicSensor()

    print ("################## Forward - distance: ",  format(distance, '.2f'))

    while True:
        if hitBlackLine() == False: #or countNegatives < 5:
            #if int(distance) < scanDistance:

            forward()
            rightMotor.ChangeDutyCycle(takeOutSpeed)
            leftMotor.ChangeDutyCycle(takeOutSpeed)
            #distance = readUltrasonicSensor()
            #reading += 1
            time.sleep (pauseTime)
            #print ("TakeITOUT distance : ", format(distance, '.2f'), "reading nr. ", reading)
        else:
            print("Somehow on the black line")
            reading = 1
            break
            #else:
            #    countNegatives += 1

    if reading == 1:
        goBack()

    print ("END takeItOut() #########################")






# Returns true everytime if finds an object withith the scanDistance
# Returns false everytime if gets to a black line
def searchForAnObject():

    global scanDistance

    turnRight()
    rightMotor.ChangeDutyCycle(25)
    leftMotor.ChangeDutyCycle(25)
    time.sleep (pauseTime)

    print ("Searching")
    while True:
        distance = readUltrasonicSensor()
        print ("Scan distance: ", distance)
        if int(distance) < scanDistance:
            '''
            adjustSleep = 0.2
            if  distance <  scanDistance * 1/3:
                forward()
                rightMotor.ChangeDutyCycle(17)
                leftMotor.ChangeDutyCycle(45)
                time.sleep(adjustSleep)
            elif distance <  scanDistance * 2/3:
                forward()
                rightMotor.ChangeDutyCycle(17)
                leftMotor.ChangeDutyCycle(45)
                time.sleep(adjustSleep * 2/3)
            else:
                forward()
                rightMotor.ChangeDutyCycle(17)
                leftMotor.ChangeDutyCycle(45)
                time.sleep (adjustSleep * 1/3)
            '''
            # Found something -> next action -> takeItOut
            STOP()
            return True

        if hitBlackLine() == True:
            STOP()
            return False


        # Actually going forward - right





def pushOutBoxes():
    countPositive = 0
    var = 0
    countTime = time.time()


    try:
        while True:

            distance = readUltrasonicSensor()
            print ("Initial Distance: ", format(distance, '.2f'), "cm")

            # If all 3 sensors are reading black we should stop, no matter what the
            # ultrasonic sensor reads

            searchResult = searchForAnObject()
            if searchResult == True:
                print ("Search result true")
                takeItOut()

            if searchResult == False:
                print ("Search result false")
                goBack()


            time.sleep (pauseTime)


            '''
            if int(distance) < scanDistance:

                adjustSleep = 0.2
                if  distance <  scanDistance * 1/3:
                    forward()
                    rightMotor.ChangeDutyCycle(17)
                    leftMotor.ChangeDutyCycle(45)
                    time.sleep(adjustSleep)
                elif distance <  scanDistance * 2/3:
                    forward()
                    rightMotor.ChangeDutyCycle(17)
                    leftMotor.ChangeDutyCycle(45)
                    time.sleep(adjustSleep * 2/3)
                else:
                    forward()
                    rightMotor.ChangeDutyCycle(17)
                    leftMotor.ChangeDutyCycle(45)
                    time.sleep (adjustSleep * 1/3)

                takeItOut()
            else:
            #if int(distance) >= scanDistance:
                #print ("otherthing ###########################################")
                #turnLeft()

                search()
                #forward()
                #rightMotor.ChangeDutyCycle(17)
                #leftMotor.ChangeDutyCycle(45)

                ################# BE SURE TO DO THAT FUCKING TO DO SHIT
                timeSleepAndCheckIfHitBlackLine(0.1)
                #time.sleep(0.1)
            '''

    except KeyboardInterrupt:
        print ()
        print ("The script was stopped by keyboard")
        print (time.time() - countTime)


    # We make sure that we re-write the content of runScript and stopScript file and also do a GPIO
    # cleanup
    finally:

        rightMotor.stop(0)
        leftMotor.stop(0)
        GPIO.cleanup()












def main ():

    # if hit black LINE : go back
    # if not, search
    startMotors()
    pushOutBoxes()

main()
