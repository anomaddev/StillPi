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

from enum import Enum
from src.relays import *
from src.display import *
from src.interface import *

version = os.environ['DISTILLERY_VERSION']
class ControllerState(Enum):
    IDLE = 0
    HEATING = 1
    COOLING = 2
    COMPLETE = 3
    ERROR = 4

state = ControllerState.IDLE

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
    update_status("PRESS START")
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
    
    global state
    state = ControllerState.HEATING
    update_status("HEATING")
    update_heater1("ON")
    update_heater2("ON")
        