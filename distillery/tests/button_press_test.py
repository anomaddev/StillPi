
from RPi.GPIO import GPIO

button_pin = 12

# Set GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_press(channel):
    print("Button pressed!")
    if GPIO.input(button_pin) == GPIO.low:
        print("Button pressed!")
    else:
        print("Button released!")

GPIO.add_event_detect(button_pin, GPIO.BOTH, callback=button_press, bouncetime=10)

try:
    while True:
        pass
finally:
    GPIO.cleanup()
