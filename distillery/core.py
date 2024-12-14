#
# DistilleryPi - A distillery controller built with Raspberry Pi and Python
# Author: Justin Ackermann
#
# Description: This file contains the core functionality of the distillery
# Date Created: 12/01/2024
#
#

import os
import time
import sys

from threading import Thread
from gpiozero import Button
from enum import Enum
from src.relays import *
from src.display import *
from src.temp import *
from src.heating import *

start_button = Button(26)
stop_button = Button(13)

version = os.environ['DISTILLERY_VERSION']

def core_function():
    print()
    print("----------------------------")
    print("Beginning core application")
    print("Version: " + version)
    print("----------------------------")
    print()

    # Setup the relays
    setup_relays()
    show_text_on_line(3, "Heater SSRs Ready")
    time.sleep(2)

    # Initialize the screen
    init_screen()
    time.sleep(2)

    # Setup the temperature sensor
    stabilize_temp()

    # TODO: Add target temp input
    update_target(int(read_target_temp()))

    # # Await start button press
    print()
    print("Press the start button to begin")
    update_status("PRESS START") 

    trigger_blink_relay(blink_relay1, RelayState.ON)
    start_button.wait_for_press()
    trigger_blink_relay(blink_relay1, RelayState.OFF)
    # time.sleep(0.5)

    # Start the program loop
    program_loop()

class ControllerState(Enum):
    IDLE = 0
    INITIAL_HEAT = 1
    MAINTAIN_HEAT = 2
    COOLING = 3
    COMPLETE = 4
    ERROR = 5

def program_loop():
    state = ControllerState.IDLE
    update_status("IDLE")

    startup = True

    time.sleep(1)

    while state != ControllerState.COMPLETE:
        if startup:
            print()
            print("Main Loop")
            print("State: " + str(state))

        match state:
            case ControllerState.IDLE:
                if startup:
                    startup = False
                    state = ControllerState.INITIAL_HEAT

                # TODO: Idle state

            case ControllerState.INITIAL_HEAT:
                inital_heat()
                state = ControllerState.MAINTAIN_HEAT

            case ControllerState.MAINTAIN_HEAT:
                maintain_heat()
                state = ControllerState.COMPLETE

            case ControllerState.COMPLETE:
                break

            case _:
                state = ControllerState.ERROR
                break

def stabilize_temp():
    update_status("STABALIZING")

    counter = 10
    while counter > 0:
        counter -= 1
        current_temp = get_temp()
        update_temp(int(current_temp))

        print('Current Temp: {0:0.2f} F'.format(current_temp))
        time.sleep(0.5)