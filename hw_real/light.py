#!/usr/bin/env python



import hw

LED_A = 6

hw.io.pinMode(LED_A, hw.io.OUTPUT)


def on_1():
	hw.io.digitalWrite(LED_A, hw.io.HIGH)
def off_1():
	hw.io.digitalWrite(LED_A, hw.io.LOW)
