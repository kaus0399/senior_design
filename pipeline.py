from datatools import *
# import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# while True:
#     if GPIO.input(10) == GPIO.HIGH:
        #instantiate microphones
upper_right_lung = Microphone(time=30, lc=60, hc=1200, pin=1, fs=1000, order=)
lower_right_lung = Microphone(time=30, lc=60, hc=1200, pin=2, fs=1000, order=)
upper_left_lung = Microphone(time=30, lc=60, hc=1200, pin=3, fs=1000)
lower_left_lung = Microphone(time=30, lc=60, hc=1200, pin=4, fs=1000)
mitrial_valve = Microphone(time=30, lc=20, hc=500, pin=5, fs=1000)
tricuspid_valve = Microphone(time=30, lc=20, hc=500, pin=6, fs=1000)
pulmonary_valve = Microphone(time=30, lc=20, hc=500, pin=7, fs=1000)
aortic_valve = Microphone(time=30, lc=20, hc=500, pin=8, fs=1000)


upper_left_lung.record()
