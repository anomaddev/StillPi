#
# temp.py - This file contains the temperature sensor functionality
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import time
import board
import digitalio
import adafruit_max31865

from src.display import *

spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs)

def get_temp(celcius=False):
    current_temp_c = sensor.temperature
    current_temp_f = sensor.temperature * 9 / 5 + 32

    if celcius:
        return current_temp_c
    else:
        return current_temp_f
    
def temp_update_loop():
    while True:
        update_temp(int(get_temp()))
        time.sleep(1)

def read_target_temp():
    # TODO: Implement target temp input
    return 100