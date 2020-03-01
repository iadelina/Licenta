from django.db import models
from .rfid import *
from django.core.validators import MinLengthValidator


# Create your models here.

class DateTimeModel(models.Model):
    current_datetime = models.DateTimeField(blank=True, null=True)

#default_value = rfid_scan()

class RFIDKeysModel(models.Model):
    key = models.CharField(max_length=13, blank=True)

class PhoneNumberModel(models.Model):
    number = models.CharField(max_length=10, blank=True)

class SecureModel(models.Model):
    minute = models.CharField(max_length=10, blank=True)


