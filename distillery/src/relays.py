#
# relays.py - This file contains th functions for relay control
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import RPi.GPIO as GPIO
import time

from enum import Enum
from display import *

relay_one = 23
relay_two = 24

class Relay(Enum):
    ONE = relay_one
    TWO = relay_two

last_trigger = {
    Relay.ONE: 0,
    Relay.TWO: 0
}

class RelayState(Enum):
    OFF = 0
    ON = 1

def setup_relays():
    GPIO.setup(relay_one, GPIO.OUT)
    GPIO.setup(relay_two, GPIO.OUT)
    print("Relays setup complete")
    print("Relay 1: " + str(relay_one))
    print("Relay 2: " + str(relay_two))
    print()
    
    try:
        test_relay(Relay.ONE)
    except Exception as e:
        if "FAILED SUCCESSFULLY" in str(e):
            print("Relay 1 test passed")
        else:
            raise Exception("Relay 1 test failed")

    time.sleep(2)
    try:
        test_relay(Relay.TWO)
    except Exception as e:
        if "FAILED SUCCESSFULLY" in str(e):
            print("Relay 2 test passed")
        else:
            raise Exception("Relay 2 test failed")
        
    time.sleep(1)
    show_text_on_line(3, "Relays OK")
    time.sleep(2)

def sleep_relays():
    GPIO.cleanup()
    print("Relays cleaned up for sleep mode")
    print()

def test_relay(relay):
    print("Relay test starting..")
    time.sleep(1)
    
    try:
        show_text_on_line(3, str(relay) + " Test ON")
        trigger_relay(relay, RelayState.ON)
        time.sleep(3)
    
        show_text_on_line(3, str(relay) + " Test OFF")
        trigger_relay(relay, RelayState.OFF)
        time.sleep(1)

        show_text_on_line(3, str(relay) + " Fail Test")
        trigger_relay(relay, RelayState.ON)
    except Exception as e:
        raise Exception("FAILED SUCCESSFULLY")

    

    print("Relay test complete")
    print()

def trigger_relay(relay, state):
    last = last_trigger[relay]

    if time.time() - last < 3:
        raise Exception("Relay " + str(relay.value) + " cannot be triggered again so soon")
    else:
        last_trigger[relay] = time.time()
        GPIO.output(relay.value, state.value)
        print("Relay " + str(relay.value) + " triggered: " + str(state))