#coding=utf-8
from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.index.as_view()),
    url(r'^r1$',views.r1),
    url(r'^r1/r2$',views.r2),
    url(r'^r1/r3$',views.r3),
    url(r'^r1/t1$',views.t1),

]
