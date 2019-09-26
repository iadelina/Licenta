#! /usr/bin/python3

import PRi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
BUZZ=14
GPIO.setup(BUZZ, GPIO.OUT)

while True:
    GPIO.output(BUZZ, GPIO.HIGH)    
    sleep(1)
    GPIO.output(BUZZ, GPIO.LOW)
    sleep(1)