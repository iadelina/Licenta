#! /usr/bin/python3

# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import os

adc = Adafruit_ADS1x15.ADS1115()

GPIO.setmode(GPIO.BOARD)
OUTDOOR_LED = 40
BUZZ=8
GPIO.setup(BUZZ, GPIO.OUT)
GPIO.setup(OUTDOOR_LED, GPIO.OUT)
GPIO.output(BUZZ, GPIO.HIGH)
# to checkk frequency
pwm_led = GPIO.PWM(OUTDOOR_LED, 100)
pwm_led.start(0)

macro='''
MAX_GAS_VALUE = 5500
GAIN = 1
MIN_TRESHOLD = 26421
MAX_TRESHOLD = 12540
MIN_TRESHOLD_LIGHTINING = 23 #6000/256
MAX_TRESHOLD_LIGHTINING = 117 #30000/256
MAX_FLOOD_TRESHOLD = 80
'''

exec(macro)

GAIN = 1
counter_gas = 1
counter_soil = 1
print('Reading ADS1x15 values, press Ctrl-C to quit...')

def trigger_alarm_and_message(seconds, phone_number, content):
     GPIO.output(BUZZ, GPIO.LOW)
     time.sleep(seconds)
     GPIO.output(BUZZ, GPIO.HIGH)
     os.system('sh /home/pi/Desktop/Licenta_latest/Licenta_senzori/send_message.sh {} {}'.format(phone_number, content))

def get_phone_number():
    pass

def soil(value):
    global counter_soil
    percent = (value - float(MIN_TRESHOLD)) * float(100) / (float(MAX_TRESHOLD) - float(MIN_TRESHOLD))
    print('Channel 0: {0:.2f} %'.format(percent))
    if percent > MAX_FLOOD_TRESHOLD:
        counter_soil += 1
        time.sleep(0.5)
        if counter_soil == 10:
            print('inundatie')
            counter_soil = 1
            trigger_alarm_and_message(1, '0740262875', 'Inundatie!')

def gas(value):
    global counter_gas
    #print('*******************************')
    #print('Channel 2: {}'.format(value))
    # Pause for half a second.
    if value > MAX_GAS_VALUE:
        print('GAS DETECTED')
        counter_gas += 1
        time.sleep(0.5)
    if counter_gas == 5:
        print('ring alarm')
        #trigger_alarm_and_message(0.2, '0740262875', 'Dectectie gaz!')
        counter = 1

def outdoor_light(value):
    value_for_duty_cycle = ((value // int(256) - int(MIN_TRESHOLD_LIGHTINING)) * int(100)) / (
                int(MIN_TRESHOLD_LIGHTINING) + int(MAX_TRESHOLD_LIGHTINING))
    # print('Channel 1: {} '.format(value_for_duty_cycle))
    if value_for_duty_cycle >= MIN_TRESHOLD_LIGHTINING:
        pwm_led.ChangeDutyCycle(value_for_duty_cycle)  # to scale between 0-100
    #    print('Duty Cycle changed!')
    else:
        if value_for_duty_cycle >= int(100):
            pwm_led.ChangeDutyCycle(100)
        else:
            pwm_led.ChangeDutyCycle(0)

while True:
    values = [0]*3
    for i in range(3):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
    #channel 0 reads soil sensor
    soil(values[0])
    #channel 1 read fotoresistor
    outdoor_light(values[1])
    #channel 2 read gas sensor
    gas(values[2])

