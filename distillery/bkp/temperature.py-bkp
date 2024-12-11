#
# temperature.py - This file contains the temperature sensor & control functionality
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
# Description: This file contains the core functionality of the distillery
#
#

from display import *
from threading import Thread

import board
import busio
import time
import random

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from scipy.signal import butter, lfilter

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
ads.address = "0x48"
ads.gain = 1

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Global to indicate if we are in the initial heating phase
isInitialHeat = True

# Temperature control variables
reached_target = False 
target_range = 3
currentTarget = 0
currentTemp = 43 # spoofed

# Max and min temperature values allowed
minTemp = 50
maxTemp = 280

# Butterworth Filter Design
def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# Apply Butterworth Filter
def butter_lowpass_filter(data, b, a):
    return lfilter(b, a, data)

# Map ADC value to discrete steps
def map_to_steps(adc_value, adc_min, adc_max, steps):
    step_size = (adc_max - adc_min) / steps
    return int((adc_value - adc_min) / step_size)

# Start reading the Target Temperature dial
def start_reading_dial():
    global currentTarget

    fs = 50.0  # Sampling frequency
    cutoff = 2.5  # Desired cutoff frequency
    order = 4
    b, a = butter_lowpass(cutoff, fs, order)

    buffer = []
    filtered_value = 0

    # Example with filtering
    adc_min = -50
    adc_max = 3100
    steps = (maxTemp - minTemp) / 5

    while True: 
        raw_value = chan.value / 10
        buffer.append(raw_value)

        if len(buffer) > fs:  # Keep only `fs` samples
            buffer = buffer[-int(fs):]
            filtered_value = butter_lowpass_filter(buffer, b, a)[-1]
        else:
            filtered_value = raw_value

        step_value = map_to_steps(filtered_value, adc_min, adc_max, steps)
        if step_value < 0:
            step_value = 0
        elif step_value > steps:
            step_value = steps

        currentTarget = int((step_value * 5) + minTemp)
        time.sleep(0.02)  # Adjust sample rate to match `fs`

def start_reading_temp():
    # Read the temperature sensor here
    # Spoofed for now
    global currentTemp
    while True:
        # Update the current temperature here
        time.sleep(random.randint(1, 3))

def activate_heater():
    global currentTemp
    global reached_target

    # Activate the heaters here
    # Spoofed for now
    while not reached_target:
        currentTemp += 1
        time.sleep(random.randint(1, 3))

    if reached_target:
        # Deactivate the heaters here
        update_status("MAINTAINING")
        update_heater1("OFF")        
        update_heater2("OFF")

def heating_loop():
    global isInitialHeat
    global reached_target
    global target_range

    t4 = Thread(target = activate_heater)

    time.sleep(0.5) # Delay for 0.5 seconds to let the dial start reading
    update_target(currentTarget)
    update_temp(currentTemp)
    update_status("STABALIZING")

    time.sleep(4) # Delay for 4 seconds to let the values stabilize
    update_target(currentTarget)
    update_temp(currentTemp)

    if isInitialHeat:
        isInitialHeat = False
        update_status("HEATING")
        update_heater1("ON")
        update_heater2("ON")
        t4.start()
    
    while True:
        update_target(currentTarget)
        update_temp(currentTemp)

        if not(currentTemp < (currentTarget + target_range)):
            reached_target = True
        elif currentTemp < (currentTarget - target_range):
            reached_target = False

        time.sleep(0.2)
