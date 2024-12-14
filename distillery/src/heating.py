#
# heating.py - This file contains program functionality for heating control
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import time
from functools import reduce

from src.display import *
from src.temp import *
from src.relays import *

current_temp = get_temp()
target_temp = 0

temp_log = []

class TempLog:
    def __init__(self, temp, time, heater1, heater2):
        self.temp = temp
        self.time = time
        self.heater1 = heater1
        self.heater2 = heater2

def inital_heat():
    print("Starting initial heat...")
    global current_temp
    global target_temp

    target_temp = read_target_temp()
    current_temp = get_temp()
    update_temp(int(current_temp))
    update_status("HEATING")

    # Turn on the heaters
    heaters_on()

    time.sleep(5) # Let the heaters warm up

    print("Starting heat loop...")
    print("Target Temp: " + str(target_temp))
    iterator = 0

    while (current_temp < (target_temp + 3)):
        iterator += 1
        target_temp = read_target_temp()
        current_temp = get_temp()

        temp_log.append(TempLog(current_temp, time.time(), "ON", "ON"))

        # Only print every 10th iteration
        if iterator % 10 == 0:
            print("Current Temp: " + str(current_temp))
            print("Rate of Change: " + str(rate_of_change()))
            

        update_target(int(target_temp))
        update_temp(int(current_temp))
        time.sleep(0.1)

    heaters_off()
    print("Initial heat complete!")

def maintain_heat():
    global target_temp
    print("Maintaining temperature...")
    update_status("MAINTAINING")

    time.sleep(3) # Let the system stabilize

    print("Target Temp: " + str(target_temp))
    h1 = False
    h2 = False
    last_trigger = 0

    interator = 0
    while interator < 1000:
        interator += 1
        target_temp = read_target_temp()
        current_temp = get_temp()

        update_target(int(target_temp))
        update_temp(int(current_temp))

        # Heaters can only be triggered every 2 seconds
        if time.time() - last_trigger > 2:
            if interator % 10 == 0:
                print("Current Temp: " + str(current_temp))
            
            last_trigger = time.time()
            if current_temp < (target_temp - 2) and not h1 and not h2:
                heaters_on()
                h1 = True
                h2 = True

            elif current_temp > (target_temp + 2) and h1 and h2:
                heaters_off()
                h1 = False
                h2 = False

            else:
                pass

        temp_log.append(TempLog(current_temp, time.time(), "ON" if h1 else "OFF", "ON" if h2 else "OFF"))
        time.sleep(0.1)

def heaters_on():
    print("Turning on both heaters...")
    trigger_SSR_relay(Relay.ONE, RelayState.ON)
    trigger_SSR_relay(Relay.TWO, RelayState.ON)

    update_heater1("ON")
    update_heater2("ON")

def heaters_off():
    print("Turning off both heaters...")
    trigger_SSR_relay(Relay.ONE, RelayState.OFF)
    trigger_SSR_relay(Relay.TWO, RelayState.OFF)

    update_heater1("OFF")
    update_heater2("OFF")

def rate_of_change():
    avg = reduce(lambda x, y: x + y, [x.temp for x in temp_log]) / len(temp_log)
    print("Average Temp: " + str(avg))