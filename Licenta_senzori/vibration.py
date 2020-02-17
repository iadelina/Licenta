
#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)
#pull_up_down=GPIO.PUD_DOWN)

def timer():
    return time.time()
def callback(channel):
        counter = 0
        print(GPIO.input(channel))
        if GPIO.input(channel):
            counter +=1
            print ("Movement Detected! {}".format(counter))
        else:
            counter = 0

def timer():
    return time.time()

GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
    #result_before = GPIO.input(channel)
    #if result_before:
    #    print("before: {}".format(result_before))
    #    start = timer()
    #    print(start)
    #    time.sleep(3)
    #    result_after = GPIO.input(channel)
    #    result_after = GPIO.input(channel)
    #    if result_after:
    #        end = timer()
    #        print(int(end)-int(start))
    time.sleep(0.1)
