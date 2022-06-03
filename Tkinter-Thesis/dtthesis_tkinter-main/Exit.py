import RPi.GPIO as GPIO
from time import sleep as slp

solenoidPin = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(solenoidPin, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        slp(2)
        GPIO.output(solenoidPin, GPIO.LOW)
        slp(10)
        GPIO.output(solenoidPin, GPIO.HIGH)
        slp(2)


