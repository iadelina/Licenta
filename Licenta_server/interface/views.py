from django.shortcuts import render
from .models import DateTimeModel
# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .tasks import read_temperature
from .sensors import TemperatureSensor

@login_required
def render_info_page(request):
    datetime_object = DateTimeModel.objects.all()
    temperature_sensor_object = TemperatureSensor(4, 'BCM')
    temperature = temperature_sensor_object.display_sensor_value() 
    #temperature = read_temperature.delay()
    return render(request, 'registration/info.html', {'datetime_object': request.user.last_login, 'temperature': temperature})

@login_required
def render_control_page(request):
    return render(request, 'registration/control.html')

