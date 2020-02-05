
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
    key_read = False
    while key_read is False:
        for key in registered_keys:
            print(key)
            id, text = reader.read()
            if str(id) != key.replace('\n', ''):
                key_read = True
                file_buffer.write(str(id)+ '\n')
                file_buffer.close()
                #os.system('sudo python3 /home/pi/Desktop/Licenta_latest/Licenta_senzori/rfid_forever.py &')
                #GPIO.cleanup()
                return str(id)
    file_buffer.close()
