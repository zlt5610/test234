"""test234 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from test234.settings import DEBUG, MEDIA_ROOT

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^student/', include('stu.urls')),
    url(r'^movie/', include('movie.urls')),
    url(r'^register/', include('register.urls')),
    url(r'^test_url/', include('test_url.urls',namespace='test_url_test',app_name='url')),
    url(r'^test_http/', include('test_http.urls')),
    url(r'^student6/', include('student6.urls')),
    url(r'^LOGIN/', include('LOGIN.urls')),
    url(r'^test_Cookie/', include('test_Cookie.urls')),
    url(r'^test_view/', include('test_view.urls')),
    url(r'^test_static/', include('test_static.urls')),
    url(r'^templates/', include('test_templates.urls')),
    url(r'^filter/', include('test_filter.urls')),
    url(r'^csrf/', include('test_csrf.urls')),
    url(r'^form/', include('test_form.urls')),
    url(r'^ajax/', include('test_AJAX.urls')),
    url(r'^ajax_register/', include('test_AJAX_register.urls')),

)

if DEBUG:
    urlpatterns+=url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
