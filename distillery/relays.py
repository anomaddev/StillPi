#
# relays.py - This file contains th functions for relay control
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import RPi.GPIO as GPIO
import time

from enum import Enum

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
    GPIO.cleanup()
    GPIO.setup(relay_one, GPIO.OUT)
    GPIO.setup(relay_two, GPIO.OUT)
    print("Relays setup complete")
    print("Relay 1: " + str(relay_one))
    print("Relay 2: " + str(relay_two))
    print()
    
    test_relays()

def sleep_relays():
    GPIO.cleanup()
    print("Relays cleaned up for sleep mode")
    print()

def test_relays():
    print("Relay test starting..")
    time.sleep(1)
    print("Relay 1 Triggering ON")
    trigger_relay(Relay.ONE, RelayState.ON)
    time.sleep(3)
    print("Relay 1 Triggering OFF")
    trigger_relay(Relay.ONE, RelayState.OFF)
    time.sleep(1)
    print("Relay 1 Triggering ON - should fail")
    trigger_relay(Relay.ONE, RelayState.ON)
    time.sleep(1)

    print("Relay test complete")
    print()

def trigger_relay(relay, state):
    last = last_trigger[relay]

    if time.time() - last < 3:
        print("Relay " + str(relay) + " cannot be triggered again so soon")
        return
    else:
        last_trigger[relay] = time.time()
        GPIO.output(relay.value, state.value)
        print("Relay " + str(relay) + " triggered: " + str(state))