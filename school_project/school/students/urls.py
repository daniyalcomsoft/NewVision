from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url('(?P<gr_no>[0-9]+)', views.detail, name='detail'),

]