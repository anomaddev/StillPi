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
from src.temp import *

version = os.environ['DISTILLERY_VERSION']

def core_function():
    print("Beginning core application")
    print("Version: " + version)
    print("---------------------------------")
    print()

    # Set GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Setup the interface & buttons
    setup_interface()

    # Setup the relays
    setup_relays()
    show_text_on_line(3, "Heater SSRs Ready")
    time.sleep(2)

    # Initialize the screen
    init_screen()
    time.sleep(2)

    # Setup the temperature sensor
    stabilize_temp()

    # # Await start button press
    # update_status("PRESS START")
    # start_button_await()
    # time.sleep(0.5)

    # Start the program loop
    program_loop()

    GPIO.cleanup()

class ControllerState(Enum):
    IDLE = 0
    INITIAL_HEAT = 1
    MAINTAIN_HEAT = 2
    COOLING = 3
    COMPLETE = 4
    ERROR = 5

def program_loop():
    state = ControllerState.IDLE
    print()

def stabilize_temp():
    update_status("STABALIZING")

    counter = 10
    current_temp = get_temp()
    update_temp(int(current_temp))
    time.sleep(1)

    while counter > 0:
        counter -= 1
        current_temp = get_temp()
        update_temp(int(current_temp))

        print('Current Temp: {0:0.2f} F'.format(current_temp))
        time.sleep(1)


def heat_to_target(target_temp):
    update_status("HEATING")
    update_target(target_temp)

    # Turn on the heaters
    trigger_relay(Relay.ONE, RelayState.ON)
    trigger_relay(Relay.TWO, RelayState.ON)

    update_heater1("ON")
    update_heater2("ON")

    time.sleep(5) # Let the heaters warm up

    current_temp = get_temp()
    update_temp(int(current_temp))

    while current_temp < target_temp:
        current_temp = get_temp()
        update_temp(int(current_temp))

        print('Current Temp: {0:0.2f} F'.format(current_temp))
        time.sleep(0.2)