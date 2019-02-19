# This script is mostly used to define global variables for our PI's PINs
# and to do the initial setup of all the GPIOs (in, out, motors)


import sys
import RPi.GPIO as GPIO
import time

# Pin numbering for the left side motors
PWMA = 11
AIN2 = 13
AIN1 = 15

# Pin numbering for the right side motors
BIN1 = 12
BIN2 = 16
PWMB = 18

# Global constants for the motors
MAXSPEED = 0.9

# For following the line we use 50 and for pushing out boxes we use 40
#frequency = 50
frequency = 40

# Initializing global variables - motors
leftSpeed = 0
rightSpeed = 0

# Pin numbering for the light sensors
leftSensor = 29
middleSensor = 31
rightSensor = 33

# Pin numbering for the ultrasonic sensor
ECHO = 38
TRIGGER = 40

# Since we always use a pair of values to start/stop a motor we define the motors as tuples

left = (AIN1, AIN2)
right = (BIN1, BIN2)

# Setting up the board
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Setting up the pins for the ultrasonic sensor
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIGGER, GPIO.OUT)


# Setting up the pins for the motors
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)


# Setting up the pins for the light sensors
GPIO.setup(leftSensor, GPIO.IN)
GPIO.setup(middleSensor, GPIO.IN)
GPIO.setup(rightSensor, GPIO.IN)

# Setting up the motors
# Left side motor
GPIO.setup(PWMA, GPIO.OUT)
leftMotor = GPIO.PWM(PWMA, frequency)

# Right side motor
GPIO.setup(PWMB, GPIO.OUT)
rightMotor = GPIO.PWM(PWMB, frequency)


# A function that starts both motors at the same time
# Initially the starting speed is 0
def startMotors():
    leftMotor.start(leftSpeed)
    rightMotor.start(rightSpeed)

# Functions for basic movement of each of the two sides

# Calling this function results in the left side motors spinning forward
def leftForward():
    GPIO.output(left, (1,0))

# Calling this function results in the left side motors spinning backwards
def leftBackwards():
    GPIO.output(left, (0,1))

# Calling this function results in the right side motors spinning forward
def rightForward():
    GPIO.output(right, (0,1))

# Calling this function results in the right side motors spinning backwards
def rightBackwards():
    GPIO.output(right, (1,0))

# More "advanced" functions that use the basic movement functions

# Calling this function results in the car going forward
# (both sides forward)
def forward():
    leftForward()
    rightForward()

# Calling this function results in the car going backwards
# (both sides backwards)
def backwards():
    leftBackwards()
    rightBackwards()

# Calling this function results in the car turning right
# (left side forward - right side backwards)
def turnRight():
    leftForward()
    rightBackwards()

# Calling this function results in the car turning left
# (left side backwards - right side forward)
def turnLeft():
    leftBackwards()
    rightForward()

# A function that stops both motors by changing the speed to 0.
# It just changes the speed to 0 because using the .stop() function from
# the GPIO package would require a new call of the .start() function from
# the same package whenever we want to stop the car for a brief period
# DISCLAIMER: We do stop the motors, but that happens in the main script, in a "finally" clause
def STOP():
    leftMotor.ChangeDutyCycle(0)
    rightMotor.ChangeDutyCycle(0)
