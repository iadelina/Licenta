#! /usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
key = "1088853604795"
RELAY=37
counter=1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY, GPIO.OUT)
GPIO.output(RELAY, GPIO.HIGH)
try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        if str(id) == key:
            if ( counter == 1):
                print("Door opened!\n ")
                GPIO.output(RELAY,GPIO.LOW)
                counter = 2
            else:
                if (counter == 2):
                    print("Door closed!\n")
                    GPIO.output(RELAY,GPIO.HIGH)
                    counter = 1
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
