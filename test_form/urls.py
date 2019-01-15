#coding=utf-8
from django.conf.urls import url
import views

urlpatterns= {
    url(r'^$', views.LoginView.as_view()),
    url(r'^form1$', views.RegisterView.as_view())
}