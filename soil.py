#! /usr/bin/python3
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1
MIN_TRESHOLD = 26421
MAX_TRESHOLD = 12540
adc.start_adc(0, gain=GAIN)

print('Reading ADS1x15 channel 0 for 5 seconds...')
start = time.time()
while (time.time() - start) <= 100.0:
    raw = adc.get_last_result()
    percent = (raw - float(MIN_TRESHOLD))*float(100)/(float(MAX_TRESHOLD) - float(MIN_TRESHOLD))
    print('Channel 0: {0:.2f} %'.format(percent))
    print('RAW: {}'.format(raw))
    time.sleep(0.5)
adc.stop_adc()

