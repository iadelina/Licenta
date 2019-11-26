from __future__ import absolute_import
from celery import shared_task
from .sensors import TemperatureSensor

@shared_task  # Use this decorator to make this a asyncronous function
def read_temperature():
   temperature_sensor_object = TemperatureSensor(4, 'BCM')
   print('chestieeeeee {}')
   return temperature_sensor_object.display_sensor_value()
