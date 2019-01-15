#coding=utf-8
from django.conf.urls import url
import views

urlpatterns=[
    url('^only$',views.only_register.as_view()),
    url('^getInfo/$',views.getInfo),
]