from django.shortcuts import render
from .models import DateTimeModel
# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .tasks import read_temperature
from .sensors import TemperatureSensor
from .led import IndoorLed
from django.http import HttpResponse
from .mail import Mail

led_object = IndoorLed(19, 'BCM')

@login_required
def render_info_page(request):
    datetime_object = DateTimeModel.objects.all()
    temperature_sensor_object = TemperatureSensor(4, 'BCM')
    temperature = temperature_sensor_object.display_sensor_value() 
    #temperature = read_temperature.delay()
    return render(request, 'registration/info.html', {'datetime_object': request.user.last_login, 'temperature': temperature})

@login_required
def render_control_page(request):
    #led_object = IndoorLed(19, 'BCM')
    state = led_object.get_current_state()
    if state == 'APRINS':
        led_object.turn_on()
    else:
        led_object.turn_off()
    return render(request, 'registration/control.html', {'led_state': state})

@login_required
def send_info_mail(request):
    state = led_object.get_current_state()
    ob = Mail()
    ob.send_mail()
    return render(request, 'registration/control.html', {'led_state': state})

@login_required
def power_on_led(request):
    #led_object = IndoorLed(19, 'BCM')
    led_object.turn_on()
    state = 'APRINS'
    return render(request, 'registration/control.html', {'led_state': state})

@login_required
def power_off_led(request):
    #led_object = IndoorLed(19, 'BCM')
    led_object.turn_off()
    state = 'STINS'
    return render(request, 'registration/control.html', {'led_state': state})
