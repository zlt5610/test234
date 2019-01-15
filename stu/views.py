# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import Student


def login_view(request):

    return render(request,'login.html')


def tologin(request):
    #获取请求参数
    sname=request.POST.get('sname','')
    spwd=request.POST.get('spwd','')
    #判断是否在数据库中存在
    count=Student.objects.filter(sname=sname,spwd=spwd).count()
    if count==1:
        return HttpResponse('登陆成功')
    return HttpResponse('登陆失败')