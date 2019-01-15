#coding=utf-8
from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.index_view),
    url(r'^get/$',views.get_view),
    url(r'^post/$',views.post_view),
    url(r'^custom/$',views.custom_view),
]