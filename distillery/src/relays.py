#
# relays.py - This file contains th functions for relay control
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import time

from gpiozero import LED
from enum import Enum

SSR1 = LED(23)
SSR2 = LED(24)

blink_relay1 = LED(20)
blink_relay2 = LED(16)

class Relay(Enum):
    ONE = SSR1
    TWO = SSR2

last_trigger = {
    Relay.ONE: 0,
    Relay.TWO: 0
}

class RelayState(Enum):
    OFF = 0
    ON = 1

def setup_relays():
    print("Setting up relays..")
    print("Solid State Relay 1: " + str(SSR1))
    print("Solid State Relay 2: " + str(SSR2))
    print("Blink Relay 1: " + str(blink_relay1))
    print("Blink Relay 2: " + str(blink_relay2))
    print()

    # Set initial states
    print("Setting initial relay states..")
    trigger_SSR_relay(Relay.ONE, RelayState.OFF)
    trigger_SSR_relay(Relay.TWO, RelayState.OFF)
    trigger_blink_relay(blink_relay1, RelayState.ON)
    trigger_blink_relay(blink_relay2, RelayState.ON)
    print()
    
    # try:
    #     test_relay(Relay.ONE)
    # except Exception as e:
    #     if "FAILED SUCCESSFULLY" in str(e):
    #         print("Relay 1 test passed")
    #     else:
    #         raise Exception("Relay 1 test failed")
    #         time.sleep(2)

    # try:
    #     test_relay(Relay.TWO)
    # except Exception as e:
    #     if "FAILED SUCCESSFULLY" in str(e):
    #         print("Relay 2 test passed")
    #     else:
    #         raise Exception("Relay 2 test failed")
    #         time.sleep(2)
        
    # show_text_on_line(3, "Relays OK")
    # time.sleep(2)

def sleep_relays():
    print("Relays cleaned up for sleep mode")
    print()

def test_relay(relay):
    print("Relay test starting..")
    time.sleep(1)
    
    try:
        trigger_SSR_relay(relay, RelayState.ON)
        time.sleep(3)
    
        trigger_SSR_relay(relay, RelayState.OFF)
        time.sleep(1)

        trigger_SSR_relay(relay, RelayState.ON)
    except Exception as e:
        raise Exception("FAILED SUCCESSFULLY")
    
def test_blink_relay():
    print("Blink Relay test starting..")
    time.sleep(1)

    trigger_blink_relay(blink_relay1, RelayState.OFF)
    time.sleep(3)

    trigger_blink_relay(blink_relay1, RelayState.ON)
    time.sleep(1)

    trigger_blink_relay(blink_relay2, RelayState.OFF)
    time.sleep(3)

    trigger_blink_relay(blink_relay2, RelayState.ON)
    time.sleep(1)

def trigger_SSR_relay(relay, state):
    last = last_trigger[relay]

    if time.time() - last < 2:
        raise Exception("Relay " + str(relay.value) + " cannot be triggered again so soon")
    else:
        last_trigger[relay] = time.time()
        if state == RelayState.ON:
            relay.value.on()
        else: 
            relay.value.off()
        print("Relay " + str(relay.value) + " triggered: " + str(state))

def trigger_blink_relay(relay, state):
    if state == RelayState.ON:
        relay.on()
    else:
        relay.off()

    print("Blink Relay " + str(relay) + " triggered: " + str(state))