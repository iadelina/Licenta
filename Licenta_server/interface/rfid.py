def write_in_file(key):
    import sys
    import os
    file_buffer = open('/home/pi/Desktop/Licenta_latest/Licenta_senzori/keys.txt', 'a+')
    file_buffer.write(str(key)+ '\n')
    file_buffer.close()

def disable_rfid_forever():
    import os
    pid = os.system('ps aux | grep rfid_forever.py | awk \'{print $2}\' | head -1')
    os.system('kill -9 {}'.format(pid))

def rfid_scan():
    import RPi.GPIO as GPIO
    from time import sleep
    import sys
    import os
    from mfrc522 import SimpleMFRC522
    pid = os.system('ps aux | grep rfid_forever.py | awk \'{print $2}\' | head -1')
    #os.system('kill -9 {}'.format(pid))
    reader = SimpleMFRC522()
    #key = "1088853604795"
    RELAY=37
    counter=1
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RELAY, GPIO.OUT)
    GPIO.output(RELAY, GPIO.HIGH)
    file_buffer = open('/home/pi/Desktop/Licenta_latest/Licenta_senzori/keys.txt', 'r+')
    registered_keys = file_buffer.readlines()
    registered_keys = [i.replace('\n','') for i in registered_keys]
    key_read = False
    print(registered_keys)
    while key_read is False:
         id, text = reader.read()
         if str(id) not in registered_keys:
             print('**************************')
             print(id)
             key_read = True
             file_buffer.close()
             return str(id)
         else:
             key_read = True
             file_buffer.close()
             return 'ini'
    file_buffer.close()
