#encoding=utf-8
from django.conf.urls import url
import views

urlpatterns=[
    url(r'^set$',views.set_CookieInfo),
    url(r'^abc$',views.get_CookieInfo),
    url(r'^login$',views.login_view),
    url(r'^tologin$',views.tologin_view),
    url(r'^session$',views.set_Session),
    url(r'^get_session$',views.get_Session),
    url(r'^login1/$',views.login1_view),
    url(r'^main/$',views.main),
]