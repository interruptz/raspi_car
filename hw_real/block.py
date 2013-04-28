#!/usr/bin/env python



import hw

DETECT_A = 5

hw.io.pinMode(DETECT_A, hw.io.INPUT)


def is_blocked():
	return hw.io.digitalRead(DETECT_A) == 0
