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
stop_button = 19

start_depressed = False
start_toggle = False

stop_depressed = False
stop_toggle = False

def start_pressed(button):
    global start_toggle
    global start_depressed

    if GPIO.input(button) == GPIO.HIGH:
        start_depressed = True
    else:
        if start_depressed:
            start_toggle = True
            start_depressed = False

def stop_pressed(button):
    global stop_toggle
    global stop_depressed

    if GPIO.input(button) == GPIO.HIGH:
        stop_depressed = True
    else:
        if stop_depressed:
            stop_toggle = True
            stop_depressed = False

def setup_interface():
    print("Setting up interfaces..")

    GPIO.setup(start_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(stop_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(start_button, GPIO.BOTH, callback=start_pressed, bouncetime=10)
    GPIO.add_event_detect(stop_button, GPIO.BOTH, callback=stop_pressed, bouncetime=10)

def start_button_await():
    print()
    print("Awaiting start button press...")
    while not start_toggle:
        pass

    print("Start button pressed!")
    GPIO.remove_event_detect(start_button)
    return


