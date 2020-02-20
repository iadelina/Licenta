def secure_mode(flag):
    counter = 1
    channel = 15
    import time
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.IN)
    BUZZ=8
    GPIO.setup(BUZZ, GPIO.OUT)
    GPIO.output(BUZZ, GPIO.HIGH)
    GPIO.add_event_detect(15, GPIO.RISING,bouncetime=200)
    if flag:
        start = time.time()
        while True:
            time.sleep(0.5)
            if GPIO.event_detected(15):
                counter +=1
                print('Miscare {}'.format(counter))
                if int(counter) == 5:
                    end = time.time()
                    print('Alerta! {}'.format(int(end)-int(start)))
                    GPIO.output(BUZZ, GPIO.LOW)
                    time.sleep(0.5)
                    GPIO.output(BUZZ, GPIO.HIGH)
                    GPIO.output(BUZZ, GPIO.LOW)
                    time.sleep(0.5)
                    GPIO.output(BUZZ, GPIO.HIGH)
                    print('inainte trigger')
                    trigger_message('0740262875', 'Alerta!')
                    start = time.time()
                    counter = 1
            else:
                counter = 1
    else:
        GPIO.remove_event_detect(15)

def trigger_message(phone_number, content):
    import os
    os.system('sh /home/pi/Desktop/Licenta_latest/Licenta_senzori/send_message.sh {} {}'.format(phone_number, content))
