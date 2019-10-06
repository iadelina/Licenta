#! /usr/bin/python3
import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO

adc = Adafruit_ADS1x15.ADS1115()
GPIO.setmode(GPIO.BOARD)
#to be tested
OUTDOOR_LED = 40
GPIO.setup(OUTDOOR_LED, GPIO.OUT)
# to checkk frequency
pwm_led = GPIO.PWM(OUTDOOR_LED, 100)
pwm_led.start(0)

GAIN = 1
#to modify
MIN_TRESHOLD_LIGHTINING = 23 #6000/256
MAX_TRESHOLD_LIGHTINING = 117 #30000/256

adc.start_adc(1, gain=GAIN)

print('Reading ADS1x15 channel 1 for 5 seconds...')
start = time.time()
while (time.time() - start) <= 100.0:
    raw = adc.get_last_result()
    value_for_duty_cycle = raw//int(256)
    print('Channel 1: {} '.format(value_for_duty_cycle))
    print('RAW: {}'.format(raw))
    if value_for_duty_cycle >= MIN_TRESHOLD_LIGHTINING:
        pwm_led.ChangeDutyCycle(50) #to scale between 0-100
        print('Duty Cycle changed!')
    else:
        pwm_led.ChangeDutyCycle(0)
    time.sleep(0.5)
adc.stop_adc()
pwm_led.stop()
