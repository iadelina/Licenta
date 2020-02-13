from django.shortcuts import render
from .models import DateTimeModel, RFIDKeysModel
# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .tasks import send_mail
from .sensors import TemperatureSensor
from .led import IndoorLed
from .rfid import *
from django.http import HttpResponse
from .mail import Mail
from .forms import AddRFIDKeysForm
from django.db.models import Q, Manager
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
#led_object = IndoorLed(35, 'BOARD')

@login_required
def render_info_page(request):
    GPIO.cleanup()
    datetime_object = DateTimeModel.objects.all()
    temperature_sensor_object = TemperatureSensor(4, 'BCM')
    temperature = temperature_sensor_object.display_sensor_value()
    GPIO.cleanup() 
    #temperature = read_temperature.delay()
    #temperature = 3
    return render(request, 'registration/info.html', {'datetime_object': request.user.last_login, 'temperature': temperature})

@login_required
def render_control_page(request):
    GPIO.cleanup()
    led_object = IndoorLed(35, 'BOARD')
    state = led_object.get_current_state()
    if state == 'APRINS':
        led_object.turn_on()
    else:
        led_object.turn_off()
    return render(request, 'registration/control.html', {'led_state': state})

@login_required
def send_info_mail(request):
    led_object = IndoorLed(35, 'BOARD')
    #ob = Mail()
    #ob.send_mail()
    #send_mail.delay()
    return render(request, 'registration/control.html', {'led_state': state})

@login_required
def power_on_led(request):
    led_object = IndoorLed(35, 'BOARD')
    led_object.turn_on()
    state = 'APRINS'
    return render(request, 'registration/control.html', {'led_state': state})

@login_required
def power_off_led(request):
    led_object = IndoorLed(35, 'BOARD')
    led_object.turn_off()
    state = 'STINS'
    return render(request, 'registration/control.html', {'led_state': state})

@login_required
def add_new_key(request):
    queryset = RFIDKeysModel.objects.all()
    if request.method == 'POST':
        form = AddRFIDKeysForm(request.POST)
        if form.is_valid():
            queryset = RFIDKeysModel.objects.create(key=form.cleaned_data['key'])
            write_in_file(form['key'].value())
            return render(request, 'registration/new_key_message.html')
            #queryset = queryset.filter(Q(id__gt=0))
    else:
        key = rfid_scan()
        #print(key)
        if key == 'ini':
            messages.info(request,'Cheia exista deja!')
            form = AddRFIDKeysForm(initial={'key': ' '})
        else:
            form = AddRFIDKeysForm(initial={'key': key})
    return render(request, 'registration/new_key.html', {'form':form, 'queryset':queryset})

@login_required
def delete_key(request):
    if request.method == 'POST':
        form = AddRFIDKeysForm(request.POST)
        if form.is_valid():
            try:
               value = RFIDKeysModel.objects.get(pk=form['key'].value())
               delete_from_file(str(value))
               value.delete()
               return render(request, 'registration/delete_key_message.html')
            except ObjectDoesNotExist:
                    queryset = RFIDKeysModel.objects.all()
                    messages.info(request,'Cheia nu exista!')
                    return render(request, 'registration/delete_key.html', {'form':form, 'queryset':queryset})
    else:
        queryset = RFIDKeysModel.objects.all()
        form = AddRFIDKeysForm(initial={'key': ''})
    return render(request, 'registration/delete_key.html', {'form':form, 'queryset':queryset})

@login_required
def display_current_keys(request):
    queryset = RFIDKeysModel.objects.all()
    return render(request, 'registration/display_current_keys.html', {'queryset':queryset})

