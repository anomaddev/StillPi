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

version = os.environ['DISTILLERY_VERSION']

def core_function():
    print("Beginning core functionality..")
    print("Version: " + version)
    print()

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

    # Await start button press
    start_button_await()
    time.sleep(2)

    # Start the program loop
    program_loop()
        
        

def stabilize_temp():
    print("Stabilizing temperature..")
    print()
    update_temp("72")

def program_loop():
    print("Starting program loop..")
    print()
    update_status("HEATING")