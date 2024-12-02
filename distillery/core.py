#
# DistilleryPi - A distillery controller built with Raspberry Pi and Python
# Author: Justin Ackermann
#
# Description: This file contains the core functionality of the distillery
# Date Created: 12/01/2024
#
#

from RPLCD.i2c import CharLCD # type: ignore
from display import *

version = "0.0.1"

start_screen(version)