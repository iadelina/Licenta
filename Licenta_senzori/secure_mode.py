import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN)
counter=1
BUZZ=8
GPIO.setup(BUZZ, GPIO.OUT)
GPIO.output(BUZZ, GPIO.HIGH)
GPIO.add_event_detect(15, GPIO.RISING,bouncetime=200)
start = time.time()

file_buffer = open('/home/pi/Desktop/Licenta_latest/Licenta_senzori/secure.txt', 'w')
file_buffer.write('1')
file_buffer.close()

def trigger_message(content):
    import os
    file_buffer = open('/home/pi/Desktop/Licenta_latest/Licenta_senzori/phone.txt','r')
    phone_number = file_buffer.read()
    print(phone_number)
    file_buffer.close()
    os.system('sh /home/pi/Desktop/Licenta_latest/Licenta_senzori/send_message.sh {} {}'.format(phone_number, content))

while True:
    time.sleep(0.5)
    if GPIO.event_detected(15):
        counter +=1
        print('Miscare {}'.format(counter))
        file_buffer = open('/home/pi/Desktop/Licenta_latest/Licenta_senzori/secure.txt', 'r')
        enable_secure_mode = file_buffer.read()
        file_buffer.close()
        if int(counter) == 5 and int(enable_secure_mode) == 1:
                end = time.time()
                print('Alerta! {}'.format(int(end)-int(start)))
                GPIO.output(BUZZ, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(BUZZ, GPIO.HIGH)
                GPIO.output(BUZZ, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(BUZZ, GPIO.HIGH)
                print('inainte trigger')
                trigger_message('Alerta hoti!')
                start = time.time()
                counter = 1
    else:
        counter = 1
    #else:
    #    GPIO.remove_event_detect(15)

