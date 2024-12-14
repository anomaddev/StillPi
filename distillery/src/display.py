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
    lcd.cursor_pos = (1, 0)
    lcd.write_string("SET:  ---F")

    # Display the heater1 status
    lcd.cursor_pos = (1, 13)
    lcd.write_string("H1: OFF")

    # Display the current temperature
    lcd.cursor_pos = (2, 0)
    lcd.write_string("REAL: ---F")

    # Display the heater2 status
    lcd.cursor_pos = (2, 13)
    lcd.write_string("H2: OFF")

    # Display the status
    lcd.cursor_pos = (0, 0)
    lcd.write_string("STATUS: STABALIZING")

def update_target(target_temp):
    temp = str(target_temp) + "F"
    lcd.cursor_pos = (1, 6)

    if len(temp) < 4:
        lcd.write_string(" ")

    lcd.write_string(temp)

def update_temp(current_temp):
    temp = str(current_temp) + "F"
    lcd.cursor_pos = (2, 6)

    if len(temp) < 4:
        lcd.write_string(" ")

    lcd.write_string(temp)

def update_status(status):
    lcd.cursor_pos = (0, 8)
    lcd.write_string(status)

    # Clear the remaining characters
    letters = len(status)
    lcd.cursor_pos = (0, 8 + letters)
    lcd.write_string(" " * (12 - letters))

def update_heater1(heater1):
    lcd.cursor_pos = (1, 17)
    lcd.write_string(heater1)

    if heater1 == "ON":
        lcd.cursor_pos = (1, 19)
        lcd.write_string(" ")

def update_heater2(heater2):
    lcd.cursor_pos = (2, 17)
    lcd.write_string(heater2)

    # Clear the remaining characters if the heater is on
    if heater2 == "ON":
        lcd.cursor_pos = (2, 19)
        lcd.write_string(" ")