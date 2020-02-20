#!/bin/sh
source /home/pi/Desktop/environment/bin/activate
systemctl stop gunicorn&
celery -A /home/pi/Desktop/Licenta_latest/Licenta_server/Licenta purge&
celery -A /home/pi/Desktop/Licenta_latest/Licenta_server/Licenta worker -l info&
python /home/pi/Desktop/Licenta_latest/Licenta_server/manage.py runserver 192.168.5.1:3001&
