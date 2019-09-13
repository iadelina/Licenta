#!/usr/bin/python
import RPi.GPIO as GPIO
from ADS1x15 import ADS1115
import time
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)
adc = ADS1115()
channel = 0
gain = 1
t = 0
#1015 is 12 bits, 1115 is 16 bits; adapt!
while True:
    data = adc.read_adc(channel, gain)
    print t, "s:", data
    t += 0.1
    time.sleep(0.1)