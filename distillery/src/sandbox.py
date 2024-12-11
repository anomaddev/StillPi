#
# sandbox.py - This file contains sandbox functionality and testing
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
# Description: This file contains experimental code and testing
#
#

import subprocess
import board
import adafruit_tca9548a

i2c = board.I2C()
adafruit_tca9548a.TCA9548A(i2c)

for channel in range(8):
    if tca[channel].try_lock():
        print("Channel {} locked".format(channel))
        addresses = tca[channel].scan()
        print([hex(address) for address in addresses if address != 0x70])
        tca[channel].unlock()