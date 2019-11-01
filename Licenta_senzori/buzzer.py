#! /usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
BUZZ=8
GPIO.setup(BUZZ, GPIO.OUT)
i=0

while True:
    while i<3:
        GPIO.output(BUZZ, GPIO.LOW)
        sleep(1)
        GPIO.output(BUZZ, GPIO.HIGH)
        sleep(1)
        i+=1
