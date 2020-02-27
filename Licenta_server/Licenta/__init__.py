from __future__ import absolute_import
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app
import sys
__all__ = ['celery_app']
sys.path.append('/home/pi/Desktop/Licenta_latest/Licenta_server/Licenta')
