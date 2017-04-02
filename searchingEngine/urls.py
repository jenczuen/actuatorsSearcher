from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax/get_actuators/$', views.filter_actuators, name='filter_actuators'),
]