from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax/get_actuators/$', views.get_actuators, name='get_actuators'),
    url(r'^ajax/get_codes/$', views.get_codes, name='get_codes'),
    url(r'^ajax/send_order/$', views.send_order, name='send_order')
]
