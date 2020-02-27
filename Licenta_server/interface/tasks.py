from __future__ import absolute_import
from celery import shared_task
from .mail import Mail
from time import sleep

@shared_task
def send_mail():
    mail_object = Mail()
    return mail_object.send_mail()

@shared_task
def run_secure_mode(self, flag, minutes):
    file_buffer = open('/home/pi/Desktop/Licenta_latest/Licenta_senzori/secure.txt', 'w')
    if flag:
        file_buffer.write('1')
        file_buffer.close()
    else:
        file_buffer.write('0')
        file_buffer.close()
        sleep(minutes*60)
        file_buffer = open('/home/pi/Desktop/Licenta_latest/Licenta_senzori/secure.txt', 'w')
        file_buffer.write('1')
        file_buffer.close()

