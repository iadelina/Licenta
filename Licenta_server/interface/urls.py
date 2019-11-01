from django.urls import path
from . import views 
app_name ='interface' 

urlpatterns = [
    path('', views.index, name='index'),
    #path('adv_search', views.adv_search, name='adv_search'), path('NA', 
    #views.not_available_link, name='NA')
]

