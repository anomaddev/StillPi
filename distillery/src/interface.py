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

start_depressed = False
start_toggle = False

def start_pressed(button):
    global start_toggle
    global start_depressed

    if GPIO.input(button) == GPIO.HIGH:
        print("Button depressed!")
        start_depressed = True
    else:
        print("Button released!")
        if start_depressed:
            start_toggle = True
            start_depressed = False

def setup_interface():
    print("Setting up interfaces..")

    GPIO.setup(start_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(start_button, GPIO.BOTH, callback=start_pressed, bouncetime=10)

def start_button_await():
    while not start_toggle:
        pass

    print("start button pressed")
    GPIO.remove_event_detect(start_button)
    return

    