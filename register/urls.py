#coding=utf-8
from django.conf.urls import url

from register import views

urlpatterns=[
    url(r'^$',views.register),
    url(r'^addstu$',views.addStu),
    url(r'^showAll/$',views.showAll),
    url(r'^detail/$',views.detail)
]