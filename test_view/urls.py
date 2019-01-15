#coding=utf-8
from django.conf.urls import url

from test_view import views

urlpatterns=[
    url(r'index$',views.IndexView.as_view())
]