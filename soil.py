#!/usr/bin/python
import RPi.GPIO as GPIO
from ADS1x15 import ADS1115
import time
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
        if GPIO.input(channel):
                print "Water Detected!"
        else:
                print "Water Detected!"
 
#GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
adc = ADS1115()
#channel = 0
gain = 1
t = 0
#1015 is 12 bits, 1115 is 16 bits; adapt!






while True:
        callback(21)
        time.sleep(1)
    data = adc.read_adc(channel, gain)
    print t, "s:", data
    t += 0.1
    time.sleep(0.1)
