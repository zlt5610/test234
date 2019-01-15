#coding=utf-8
from django.conf.urls import url
import views
urlpatterns=[
    url(r'^upload/$',views.upload),
    url(r'^toupload/$',views.toupload),
    url(r'^showall/$',views.showall),
    url(r'^download1/$',views.download1),
]