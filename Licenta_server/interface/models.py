from django.db import models
from .rfid import *

# Create your models here.

class DateTimeModel(models.Model):
    current_datetime = models.DateTimeField(blank=True, null=True)

#default_value = rfid_scan()

class RFIDKeysModel(models.Model):
    key = models.CharField(max_length=13, blank=True)
