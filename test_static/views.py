# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.template import Template,Context,loader
import os

class index(View):
    def get(self,request):
        return render(request,'test_static_index.html')


def r1(request):
    with open(os.path.join(os.getcwd(),'templates','r.html'),'rb') as fr:
        content=fr.read()
    #创建模板对象
    t=Template(content)
    c=Context({'uname':'zhangsan'})
    #将参数传递给模板页面进行渲染，生成的是页面的字符串
    renderStr=t.render(c)
    return HttpResponse(renderStr)


def r2(request):
    t=loader.get_template('r.html')
    renderStr=t.render({'uname':'lisi'})
    return HttpResponse(renderStr)


def r3(request):
    return render(request,'r.html',{'uname':'wangwu'})


def t1(request):
    return render(request,'t.html')