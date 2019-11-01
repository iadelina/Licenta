"""Licenta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path
#import debug_toolbar
from django.conf.urls import url, include
#from rest_framework import routers
from interface import views
#router = routers.SimpleRouter() router.register(r'api/rfs/tests', 
#views.TestsViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^', include(router.urls)),
 #   url(r'^__debug__/', include(debug_toolbar.urls)),
    path('interface/', include('interface.urls', namespace='index')),
    path('', include('interface.urls')),
    #path('adv_search/', include('rfs_tests.urls', 
    #namespace='adv_search')), path('NA/', include('rfs_tests.urls', 
    #namespace='NA'))
]
