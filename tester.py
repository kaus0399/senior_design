from datatools import *
import asyncio
# import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# while True:
#     if GPIO.input(10) == GPIO.HIGH:
        #instantiate microphones
test_microphone = Microphone(name="test_microphone.wav" time=30, lc=60, hc=1200, pin=1, fs=1000, order=5, pin=)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
button_num = 
button = GPIO.setup(button_num, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if button == GPIO.HIGH:
        test_microphone.record(button)
