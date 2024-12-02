from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8)
lcd.clear()

lcd.cursor_pos = (2, 1)
lcd.write_string('Hello World')
