# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime
# Create your views here.
def index_view(request):
    list1=['a1','a2','a3']
    dic1={'k1':'v1','k2':'v2'}
    today=datetime.datetime.today()

    str1='<h1>hello</h1>'

    return render(request,'index_templates.html',{'uname':'zhangsan','list1':list1,'dic1':dic1,'today':today,'str1':str1})


def index1_view(request):
    return render(request,'template_index.html')