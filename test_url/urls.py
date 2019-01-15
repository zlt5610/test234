# coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.query_view),
    url(r'^query2/(\d+)/(\d+)$', views.query_view2),
    url(r'^query3/(?P<uname>[a-zA-Z]{8})/(?P<pwd>\d{3})$', views.query_view3),
    url(r'^query4/$', views.query_view4, {'hello': '123'}),
    url(r'^query5/$', views.query_view5, name='query5'),
    url(r'^query6/$', views.query_view6)
]
