#
# sandbox.py - This file contains sandbox functionality and testing
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
# Description: This file contains experimental code and testing
#
#

import RPi.GPIO as GPIO
import time

relay_one = 23
relay_two = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(relay_one, GPIO.OUT)
GPIO.setup(relay_two, GPIO.OUT)

def relay_test():
    print("Relay test starting..")
    time.sleep(1)
    print("Relay 1 Triggering ON")
    GPIO.output(relay_one, GPIO.HIGH)
    time.sleep(3)
    print("Relay 1 Triggering OFF")
    GPIO.output(relay_one, GPIO.LOW)
    time.sleep(1)
    print("Relay 2 Triggering ON")
    GPIO.output(relay_two, GPIO.HIGH)
    time.sleep(3)
    print("Relay 2 Triggering OFF")
    GPIO.output(relay_two, GPIO.LOW)
    time.sleep(1)

    print("Relay test complete")

relay_test()

GPIO.cleanup()