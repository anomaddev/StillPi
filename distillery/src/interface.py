#
# interface.py - This file contains the interactive interface functionality
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import time

import RPi.GPIO as GPIO

from core import *

start_button = 26

def start_pressed(button):
    if GPIO.input(button) == GPIO.HIGH:
        print("Button depressed!")
    else:
        print("Button released!")

def setup_interface():
    print("Setting up interfaces..")

    GPIO.setup(start_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(start_button, GPIO.BOTH, callback=start_pressed, bouncetime=10)
    