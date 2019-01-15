#coding=utf-8
from django.conf.urls import url

from movie import views

urlpatterns=[
    url(r'^$',views.index_view)
]