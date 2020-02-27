#! /usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import sys
import os
from mfrc522 import SimpleMFRC522
#reader = SimpleMFRC522()
#key = "1088853604795"
RELAY=37
counter=1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY, GPIO.OUT)
GPIO.output(RELAY, GPIO.HIGH)
print("Hold a tag near the reader")
while True:
    RELAY=37
    GPIO.setup(RELAY, GPIO.OUT)
    reader = SimpleMFRC522()
    id, text = reader.read()
    print('****')
    file_buffer = open('/home/pi/Desktop/Licenta_latest/Licenta_senzori/keys.txt', 'r+')
    registered_keys = file_buffer.readlines()
    print(registered_keys)
    for key in registered_keys:
        print(key)
        if str(id) == key.replace('\n', ''):
            if ( counter == 1):
                print("Door opened!\n ")
                GPIO.output(RELAY,GPIO.LOW)
                counter = 2
            else:
                if (counter == 2):
                    print("Door closed!\n")
                    GPIO.output(RELAY,GPIO.HIGH)
                    counter = 1
                    file_buffer = open('/home/pi/Desktop/Licenta_latest/Licenta_senzori/secure.txt', 'w')
                    file_buffer.write('1')
                    file_buffer.close()
    sleep(0.5)
#GPIO.cleanup()
#exit=os.getpid()
#os.system('kill -9 {}'.format(exit))
