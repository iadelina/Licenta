counter = 1
channel = 15
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN)
BUZZ=8
GPIO.setup(BUZZ, GPIO.OUT)
GPIO.add_event_detect(15, GPIO.RISING,bouncetime=200)
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
             time.sleep(1)
             GPIO.output(BUZZ, GPIO.HIGH)
             start = time.time()
             counter = 1
    else:
        counter = 1
        print('***')
   # GPIO.remove_event_detect(15)
   # channel = GPIO.wait_for_edge(15, GPIO.FALLING, timeout=5000)
   # if channel is None:
   #     print('Timeout occurred')
   # else:
   #     print('Edge detected on channel', channel)
   # GPIO.remove_event_detect(15)
