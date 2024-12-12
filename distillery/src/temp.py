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

loop_active = True

current_temp_c = 0
current_temp_f = 0

target_temp = 180

def temp_sensor_loop():
    global current_temp_c
    global current_temp_f

    while loop_active:
        current_temp_c = sensor.temperature
        current_temp_f = sensor.temperature * 9 / 5 + 32

        # print('Temperature: {0:0.2f} F'.format(current_temp_f))
        update_temp(int(current_temp_f))
        time.sleep(1) # Sleep for 1 second