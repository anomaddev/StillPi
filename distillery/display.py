#
# display.py - This file contains the lcd display functionality
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
# Description: This file contains the core functionality of the distillery
#
#

from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8)

def start_screen():
    lcd.clear() # Clear the screen

    # Display the welcome message
    lcd.cursor_pos = (0, 2)
    lcd.write_string("DistilleryPi")