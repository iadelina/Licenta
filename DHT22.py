import Adafruit_DHT as dht
from time import sleep
#Set DATA pin
DHT = 4
while True:
    #Read Temp and Hum from DHT22
    humidity,temperature = dht.read_retry(dht.DHT22, DHT)
    #Print Temperature and Humidity on Shell window
    print('Temp={0:0.1f}*C'.format(temperature))
    sleep(5)