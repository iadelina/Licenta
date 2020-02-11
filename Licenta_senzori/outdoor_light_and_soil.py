
#! /usr/bin/python3


# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
adc = Adafruit_ADS1x15.ADS1115()

GPIO.setmode(GPIO.BOARD)
OUTDOOR_LED = 40
GPIO.setup(OUTDOOR_LED, GPIO.OUT)
# to checkk frequency
pwm_led = GPIO.PWM(OUTDOOR_LED, 100)
pwm_led.start(0)

macro='''
MAX_VALUE = 100
GAIN = 1
MIN_TRESHOLD = 26421
MAX_TRESHOLD = 12540
MIN_TRESHOLD_LIGHTINING = 23 #6000/256
MAX_TRESHOLD_LIGHTINING = 117 #30000/256

'''

exec(macro)

GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
while True:
    values = [0]*2
    for i in range(2):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
    #channel 0 reads soil sensor
    percent = (values[0] - float(MIN_TRESHOLD))*float(100)/(float(MAX_TRESHOLD) - float(MIN_TRESHOLD))
    print('Channel 0: {0:.2f} %'.format(percent))
    print('| {0:>6} | {1:>6} |'.format(*values))
    #channel 1 read fotoresistor
    value_for_duty_cycle = ((values[1]//int(256) - int(MIN_TRESHOLD_LIGHTINING))*int(100))/(int(MIN_TRESHOLD_LIGHTINING) + int(MAX_TRESHOLD_LIGHTINING))
    print('Channel 1: {} '.format(value_for_duty_cycle))
    if value_for_duty_cycle >= MIN_TRESHOLD_LIGHTINING:
        pwm_led.ChangeDutyCycle(value_for_duty_cycle) #to scale between 0-100
        print('Duty Cycle changed!')
    else:
        if value_for_duty_cycle >= int(100):
            pwm_led.ChangeDutyCycle(100)
        else:
            pwm_led.ChangeDutyCycle(0)
    # Pause for half a second.
    time.sleep(0.5)
