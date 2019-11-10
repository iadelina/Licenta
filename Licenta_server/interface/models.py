from django.db import models

# Create your models here.

class DateTimeModel(models.Model):
    current_datetime = models.DateTimeField(blank=True, null=True)
