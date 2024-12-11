#
# DistilleryPi - A distillery controller built with Raspberry Pi and Python
# Author: Justin Ackermann
#
# Description: This file contains the core functionality of the distillery
# Date Created: 12/01/2024
#
#

from threading import Thread
import RPi.GPIO as GPIO

import os
import time
import sys

from src.relays import *
from src.display import *
from src.interface import *

initial_load = True
version = os.environ['DISTILLERY_VERSION']

def core_function():
    global initial_load
    print("Beginning core functionality..")
    print("Version: " + version)
    print()

    if initial_load:
        initial_load = False
        
        # Set GPIO mode
        GPIO.setmode(GPIO.BCM)
        
        # Setup the relays
        setup_relays()
        show_text_on_line(3, "Heater SSRs Ready")
        time.sleep(2.5)

        setup_interface()
        show_text_on_line(3, "Buttons Active")
        time.sleep(2.5)

        # Initialize the screen
        init_screen()
        time.sleep(2.5)

        # Get initial temperature reading
        stabilize_temp()

def stabilize_temp():
    print("Stabilizing temperature..")
    print()
    update_temp("72")

def program_loop():
    print("Starting program loop..")
    print()