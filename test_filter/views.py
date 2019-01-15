# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def filter_view(request):
    return render(request,'filter.html',{'num':10,'char':'abc'})


def filter2_view(request):
    str1='#### 配置路由'
    str2='helloworld'
    return render(request,'filter2.html',{'str1':str1,'str2':str2})