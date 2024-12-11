#
# display.py - This file contains the lcd display functionality
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import time

from RPLCD.i2c import CharLCD # type: ignore

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8, backlight_enabled=True)

def lcd_show_message(message):
    lcd.clear() # Clear the screen
    lcd.write_string(message)

def clear_line(line):
    lcd.cursor_pos = (line, 0)
    lcd.write_string(" " * 20)

def show_text_on_line(line, text, center=True):
    write = text
    if center:
        write = text.center(20, " ")

    lcd.cursor_pos = (line, 0)
    lcd.write_string(write)

def start_screen(version):
    lcd.clear() # Clear the screen

    # Display the welcome message
    lcd.cursor_pos = (0, 4)
    lcd.write_string("DistilleryPi")
    lcd.cursor_pos = (1, 7)
    lcd.write_string("v" + version)
    lcd.cursor_pos = (3, 3)
    lcd.write_string("Initializing..")

def init_screen():
    lcd.clear() # Clear the screen

    # Display the target temperature
    lcd.cursor_pos = (0, 0)
    lcd.write_string("SET:  ---F")

    # Display the heater1 status
    lcd.cursor_pos = (0, 13)
    lcd.write_string("H1: OFF")

    # Display the current temperature
    lcd.cursor_pos = (1, 0)
    lcd.write_string("REAL: ---F")

    # Display the heater2 status
    lcd.cursor_pos = (1, 13)
    lcd.write_string("H2: OFF")

    # Display the status
    lcd.cursor_pos = (3, 0)
    lcd.write_string("STATUS: STABALIZING")

def update_screen(target_temp, current_temp, status, heater1, heater2):
    lcd.clear() # Clear the screen

    # Display the target temperature
    lcd.cursor_pos = (0, 0)
    lcd.write_string("TARGET:  ")
    update_target(target_temp)

    # Display the heater1 status
    lcd.cursor_pos = (0, 14)
    lcd.write_string("H1 ")
    update_heater1(heater1)

    # Display the current temperature
    lcd.cursor_pos = (1, 0)
    lcd.write_string("CURRENT: ")
    update_temp(current_temp)

    # Display the heater2 status
    lcd.cursor_pos = (1, 14)
    lcd.write_string("H2 ")
    update_heater2(heater2)

    # Display the status
    lcd.cursor_pos = (3, 0)
    lcd.write_string("STATUS: ")
    update_status(status)

def update_target(target_temp):
    temp = str(target_temp) + "F"
    lcd.cursor_pos = (0, 9)
    lcd.write_string(temp)

    if len(temp) < 4:
        lcd.cursor_pos = (0, 12)
        lcd.write_string(" ")

def update_temp(current_temp):
    temp = str(current_temp) + "F"
    lcd.cursor_pos = (1, 9)
    lcd.write_string(temp)

    if len(temp) < 4:
        lcd.cursor_pos = (1, 12)
        lcd.write_string(" ")

def update_status(status):
    lcd.cursor_pos = (3, 8)
    lcd.write_string(status)

    # Clear the remaining characters
    letters = len(status)
    lcd.cursor_pos = (3, 8 + letters)
    lcd.write_string(" " * (12 - letters))

def update_heater1(heater1):
    lcd.cursor_pos = (0, 17)
    lcd.write_string(heater1)

    # Clear the remaining characters if the heater is on
    if heater1 == "ON":
        lcd.cursor_pos = (0, 19)
        lcd.write_string(" ")

def update_heater2(heater2):
    lcd.cursor_pos = (1, 17)
    lcd.write_string(heater2)

    # Clear the remaining characters if the heater is on
    if heater2 == "ON":
        lcd.cursor_pos = (1, 19)
        lcd.write_string(" ")

def spoof_display():
    time.sleep(2)  # Delay for 2 seconds
    update_status("STABALIZING")
    update_target(180)
    update_temp(80)

    time.sleep(2)  # Delay for 2 seconds
    update_status("HEATING")
    update_heater1("ON")
    update_heater2("ON")

    # Spoofing updates
    time.sleep(1) 
    update_temp(82)
    time.sleep(3)
    update_target(195)
    time.sleep(2)
    update_status("READY")
    time.sleep(5)
    update_status("HEATING")
    time.sleep(0.5)
    update_heater1("ON")
    update_heater2("ON")
    time.sleep(2)
    update_temp(84)
    time.sleep(2)
    update_temp(86)
    time.sleep(2)
    update_temp(88)
    time.sleep(2)
    update_temp(90)
    time.sleep(2)
    update_temp(101)
    time.sleep(2)
    update_temp(108)
    time.sleep(2)
    update_temp(121)
    time.sleep(2)
    update_temp(130)
    time.sleep(2)
    update_temp(140)
    time.sleep(2)
    update_temp(150)
    time.sleep(2)
    update_temp(172)
    time.sleep(2)
    update_temp(187)
    time.sleep(2)
    update_temp(192)

    time.sleep(2)  # Delay for 2 seconds
    update_status("MAINTAINING")
    update_heater1("ON")
    update_heater2("OFF")