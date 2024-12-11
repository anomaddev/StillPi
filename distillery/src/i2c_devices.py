#
# i2cexpander.py - This file contains the expander functionality to enable multiple I2C devices
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import time

from RPLCD.i2c import CharLCD # type: ignore

import board
import adafruit_tca9548a

# Create I2C bus as normal
i2c = board.I2C()

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

TCA_ADDR = 0x70

def select_channel(bus, channel):
    if 0 <= channel <= 7:
        bus.write_byte(TCA_ADDR, 1 << channel)
    else:
        raise ValueError("Channel must be in range 0-7")