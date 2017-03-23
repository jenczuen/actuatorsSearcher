from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^api/data$', views.DataView1.as_view()),
    url(r'^api/dupa$', views.DataView2.as_view())
]