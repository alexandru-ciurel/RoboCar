from initialSetup import *

# Short description of what a PID controller is:
# [A PID controller is a control loop feedback mechanism widely used in
# industrial control systems and a variety of other applications requiring
# continuously modulated control. A PID controller continuously calculates an
# error value e(t) as the difference between a desired setpoint (SP) and a
# measured process variable (PV) and applies a correction based on proportional,
# integral, and derivative terms (denoted P, I, and D respectively), hence
# the name.]
#
# In the end we've only used the "P" part of it for our line following challenge
#
#
# In our case, the desired setpoint is actually when the robocar is perfectly
# centered on the black line [ middle sensor detecting black while the left and
# right sensors detect white]. So when we have this situation we are having no
# error (error = 0). When we calculate the error, we also assign a certain value
# to the "direction" global variable which represents the direction that the car
# needs to go. When the error = 0 the direction is "forward".
# Other situations:
# error = 1 when middle, right are on black -> direction = "right"
# error = -1 when left, middle are on black -> direction = "left"
# error = 1.5 when only right is on black  -> direction = "right"
# error = -1.5 when only left is on black -> direction = "left"
# error = 0 when all 3 on black -> direction = "forward"
#
# We calculate the error using the "calculateError()" function and based on
# error we calculate the measured process variable (PV)-- which is called
# "PID.value" in our scripts - using the "calculatePID()" function
#
#
# Global variables used for calculating the PIDvalue
#
# The initialSpeed, KS, KP have some certain specific values. We came up with
# this values after a lot of trial and error test with our robocar.


KP = 34
KI = 0
KD = 0

P = 0
I = 0
Derivative = 0

direction = ""

error = 0
previousError = 0
previousI = 0

PIDvalue = 0

# Calcualting the error which is one of the most important variables in the PID algorithm
def calculateError (sensors):

    global error

    if sensors[0] == 1 and sensors[1] == 0 and sensors[2] == 0:
        error = -1.5
        direction = "left"
    elif sensors[0] == 1 and sensors[1] == 1 and sensors[2] == 0:
        error = -1
        direction = "left"
    elif sensors[0] == 0 and sensors[1] == 1 and sensors[2] == 0 or \
         sensors[0] == 1 and sensors[1] == 0 and sensors[2] == 1 or \
         sensors[0] == 1 and sensors[1] == 1 and sensors[2] == 1:
        error = 0
        direction = "forward"
    elif sensors[0] == 0 and sensors[1] == 1 and sensors[2] == 1:
        error = 1
        direction = "right"
    elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] == 1:
        error = 1.5
        direction = "right"



# A function that calculates the PIDvalue based on a PID algorithm
def calculatePID():
    global KP
    global KI
    global KD

    global P
    global I
    global Derivative

    global error
    global previousError
    global previousI

    global PIDvalue

    P = error
    Derivative = error - previousError
    I = I + error # this is the total error that keeps adding
    PIDvalue = (KP * P) + (KI * I) + (KD * Derivative)
    previousError = error
