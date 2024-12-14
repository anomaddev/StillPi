#
# programs.py - This file contains program functionality for different states
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import time

from src.display import *
from src.temp import *
from src.relays import *

current_temp = get_temp()
target_temp = 0

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
    while current_temp < (target_temp + 3):
        iterator += 1
        target_temp = read_target_temp()
        current_temp = get_temp()

        # Only print every 10th iteration
        if iterator % 10 == 0:
            print("Current Temp: " + str(current_temp))

        update_target(int(target_temp))
        update_temp(int(current_temp))
        time.sleep(0.1)

    print("Initial heat complete!")
    heaters_off()

def maintain_heat():
    global target_temp
    print("Maintaining temperature...")
    update_status("MAINTAINING")

    print("Target Temp: " + str(target_temp))
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
            if current_temp < (target_temp - 2):
                heaters_on()
            elif current_temp > (target_temp + 2):
                heaters_off()
            else:
                pass

        time.sleep(0.1)

def heaters_on():
    print("Turning on both heaters...")
    trigger_relay(Relay.ONE, RelayState.ON)
    trigger_relay(Relay.TWO, RelayState.ON)

    update_heater1("ON")
    update_heater2("ON")

def heaters_off():
    print("Turning off both heaters...")
    trigger_relay(Relay.ONE, RelayState.OFF)
    trigger_relay(Relay.TWO, RelayState.OFF)

    update_heater1("OFF")
    update_heater2("OFF")