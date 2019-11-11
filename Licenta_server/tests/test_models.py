from django.test import TestCase
from interface.models import DateTimeModel
import datetime

class DateTimeModelTest(TestCase):
    datetime = datetime.datetime.now()
    @classmethod
    def setUpTestData(cls):
        DateTimeModel.objects.create(current_datetime='2019-09-08 17:27+0200')

    def test_current_datetime_label(self):
        datetime_field = DateTimeModel.objects.get(id=1)
        field_label = datetime_field._meta.get_field('current_datetime').verbose_name
        self.assertEquals(field_label, 'current datetime')

    def test_current_datetime_is_blank(self):
        datetime_field = DateTimeModel.objects.get(id=1)
        blank = datetime_field._meta.get_field('current_datetime').blank
        self.assertEquals(blank, True)

    def test_current_datetime_is_null(self):
       datetime_field = DateTimeModel.objects.get(id=1)
       null_field = datetime_field._meta.get_field('current_datetime').null
       self.assertEquals(null_field, True)
