from django.urls import path, include 
from . import views 
app_name ='interface'

urlpatterns = [
    path('render_info_page', views.render_info_page, name='render_info_page'),
    #path('adv_search', views.adv_search, name='adv_search'), path('NA', 
    #views.not_available_link, name='NA')
#    path('interface/',include('django.contrib.auth.urls'))
]

