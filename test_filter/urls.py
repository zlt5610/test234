#coding=utf-8
from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.filter_view),
    url(r'^f2$',views.filter2_view)
]