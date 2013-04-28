#!/usr/bin/env python 

import hw

MOTOR_L_A = 4
MOTOR_L_B = 3
MOTOR_R_A = 1
MOTOR_R_B = 0

# I/O Setting
hw.io.pinMode(MOTOR_L_A, hw.io.OUTPUT)
hw.io.pinMode(MOTOR_L_B, hw.io.OUTPUT)
hw.io.pinMode(MOTOR_R_A, hw.io.OUTPUT)
hw.io.pinMode(MOTOR_R_B, hw.io.OUTPUT)


def left_forward():
    hw.io.digitalWrite(MOTOR_L_A, hw.io.HIGH)
    hw.io.digitalWrite(MOTOR_L_B, hw.io.LOW)

def left_backward():
    hw.io.digitalWrite(MOTOR_L_A, hw.io.LOW)
    hw.io.digitalWrite(MOTOR_L_B, hw.io.HIGH)

def left_stop():
    hw.io.digitalWrite(MOTOR_L_A, hw.io.LOW)
    hw.io.digitalWrite(MOTOR_L_B, hw.io.LOW)

def right_forward():
    hw.io.digitalWrite(MOTOR_R_A, hw.io.HIGH)
    hw.io.digitalWrite(MOTOR_R_B, hw.io.LOW)

def right_backward():
    hw.io.digitalWrite(MOTOR_R_A, hw.io.LOW)
    hw.io.digitalWrite(MOTOR_R_B, hw.io.HIGH)

def right_stop():
    hw.io.digitalWrite(MOTOR_R_A, hw.io.LOW)
    hw.io.digitalWrite(MOTOR_R_B, hw.io.LOW)
