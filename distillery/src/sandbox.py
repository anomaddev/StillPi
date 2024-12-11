#
# sandbox.py - This file contains sandbox functionality and testing
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
# Description: This file contains experimental code and testing
#
#

import subprocess
import smbus2
import board
import adafruit_tca9548a

import time

from RPLCD.i2c import CharLCD # type: ignore

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
    
bus = smbus2.SMBus(1)

select_channel(bus, 2)
select_channel(bus, 7)

# for channel in range(8):
#     if tca[channel].try_lock():
#         print("Channel {} locked".format(channel))
#         addresses = tca[channel].scan()
#         print([hex(address) for address in addresses if address != 0x70])
#         tca[channel].unlock()


lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8, backlight_enabled=True)
lcd.write_string("Hello, world!")