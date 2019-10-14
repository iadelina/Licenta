#! /usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
key = "1088853604795"
RELAY=37
GPIO.setmode(GPIO.BOARD)
try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        if str(id) == key:
            print("Door opened!\n")
            GPIO.output(RELAY, HIGH)
            sleep(2)
            GPIO.output(RELAY, LOW)
            sleep(0.5)
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
