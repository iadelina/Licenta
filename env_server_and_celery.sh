#!/bin/sh

#systemctl stop gunicorn&
/home/pi/Desktop/environment/bin/python3.5  /home/pi/Desktop/Licenta_latest/Licenta_server/manage.py runserver 192.168.5.1:3000&
#/home/pi/Desktop/environment/bin/python3.5 fix_path.py&
cd /home/pi/Desktop/Licenta_latest/Licenta_server
echo yes | /home/pi/Desktop/environment/bin/celery -A Licenta purge&
#/home/pi/Desktop/Licenta_latest/Licenta_server/Licenta
/home/pi/Desktop/environment/bin/celery -A Licenta worker  -l info&

