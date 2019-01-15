# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    m=request.method
    path=request.path
    schme=request.scheme
    print '请求方式：%s'%m
    print '访问地址：%s'%path
    print '协议类型：%s'%schme
    print request.META
    return HttpResponse('hello')


def setResponse(request):
    resp=HttpResponse('<h1>hello httpResponse</h1>',content_type='text/html;charset=utf-8')
    #resp.__setitem__('Hello',123)
    resp.setdefault('Server','SXTServer')
    return resp