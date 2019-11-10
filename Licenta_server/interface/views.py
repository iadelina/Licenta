from django.shortcuts import render
from .models import DateTimeModel

# Create your views here.

from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required
def render_info_page(request):
    datetime_object = DateTimeModel.objects.all()
    return render(request, 'registration/info.html', {'datetime_object': request.user.last_login})
