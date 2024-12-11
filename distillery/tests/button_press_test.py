
import RPi.GPIO as GPIO

button_pin = 6

# Set GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_press(button):
    print("Button pressed!")
    if GPIO.input(button) == GPIO.LOW:
        print("Button pressed!")
    else:
        print("Button released!")

GPIO.add_event_detect(button_pin, GPIO.BOTH, callback=button_press, bouncetime=10)

try:
    while True:
        pass
finally:
    GPIO.cleanup()
