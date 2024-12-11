#
# DistilleryPi - A distillery controller built with Raspberry Pi and Python
# Author: Justin Ackermann
#
# Description: This file contains the core functionality of the distillery
# Date Created: 12/01/2024
#
#

from threading import Thread
from RPLCD.i2c import CharLCD # type: ignore
import RPi.GPIO as GPIO

import os
import time

from src.relays import *
from src.display import *

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8, backlight_enabled=True)

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

# Show initial screen for at least 5 seconds
# start_screen(version)
# time.sleep(3)

# def setup():
#     # Set GPIO mode
#     GPIO.setmode(GPIO.BCM)

#     # Setup the relays
#     setup_relays()

# # Setup the controller
# setup()

# # Sleep mode
# def sleep():
#     # Cleanup the relay GPIOs
#     sleep_relays()

# # Sleep the controller
# sleep()

# Set initial values
# update_screen("--", "--", "STARTUP", "OFF", "OFF")

# t1 = Thread(target = start_reading_dial)
# t2 = Thread(target = start_reading_temp)
# t3 = Thread(target = heating_loop)

# print("Starting threads..")
# t1.start()
# t2.start()
# t3.start()