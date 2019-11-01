#! /usr/bin/python3
import time
import Adafruit_ADS1x15

macro='''
MAX_VALUE = 100
GAIN = 1
MIN_TRESHOLD = 26421
MAX_TRESHOLD = 12540
'''

exec(macro)

adc = Adafruit_ADS1x15.ADS1115()
adc.start_adc(0, gain=GAIN)

print('Reading ADS1x15 channel 0 for 5 seconds...')
start = time.time()
while (time.time() - start) <= MAX_VALUE:
    raw = adc.get_last_result()
    percent = (raw - float(MIN_TRESHOLD))*float(100)/(float(MAX_TRESHOLD) - float(MIN_TRESHOLD))
    print('Channel 0: {0:.2f} %'.format(percent))
    print('RAW: {}'.format(raw))
    time.sleep(0.5)
adc.stop_adc()

