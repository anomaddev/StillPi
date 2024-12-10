#
# relays.py - This file contains th functions for relay control
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import RPi.GPIO as GPIO
import time

relay_one = 23
relay_two = 24

def setup_relays():
    GPIO.setup(relay_one, GPIO.OUT)
    GPIO.setup(relay_two, GPIO.OUT)

def test_relays():
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
    GPIO.cleanup()