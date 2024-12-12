#
# sandbox.py - This file contains sandbox functionality and testing
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
# Description: This file contains experimental code and testing
#
#

import board
import digitalio
import adafruit_max31865

spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, wires=3)

print('Temperature: {0:0.3f}C'.format(sensor.temperature))
print('Resistance: {0:0.3f} Ohms'.format(sensor.resistance))