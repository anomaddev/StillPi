#
# DistilleryPi - A distillery controller built with Raspberry Pi and Python
# Author: Justin Ackermann
#
# Description: This file contains the core functionality of the distillery
# Date Created: 12/01/2024
#
#

# I2C Devices
from RPLCD.i2c import CharLCD # type: ignore

from display import *
from temperature import *

from threading import Thread

import time

version = "0.0.1"

# Show initial screen for at least 5 seconds
start_screen(version)
time.sleep(1)

# Set initial values
update_screen("--", "--", "STARTUP", "OFF", "OFF")

t1 = Thread(target = start_reading_dial)
t2 = Thread(target = run_heating)

print("Starting threads..")
t1.start()
t2.start()