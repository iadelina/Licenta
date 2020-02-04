
def rfid_scan():
    import RPi.GPIO as GPIO
    from time import sleep
    import sys
    import os
    from mfrc522 import SimpleMFRC522
    reader = SimpleMFRC522()
    #key = "1088853604795"
    RELAY=37
    counter=1
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RELAY, GPIO.OUT)
    GPIO.output(RELAY, GPIO.HIGH)
    id, text = reader.read()
    print('****')
    file_buffer = open('/home/pi/Desktop/Licenta_latest/Licenta_senzori/keys.txt', 'r+')
    registered_keys = file_buffer.readlines()
    print(registered_keys)
    key_read = False
    while key_read is False:
        for key in registered_keys:
            print(key)
            id, text = reader.read()
            if str(id) == key.replace('\n', ''):
                key_read = True
                file_buffer.write(str(id)+ '\n')
                file_buffer.close()
                return str(id)
    file_buffer.close()
