# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from register.models import *


def register(request):
    return render(request,'register.html')


def addStu(request):
    #获取请求参数，用户输入的信息
    sname=request.POST.get('sname')
    cname=request.POST.get('cname')
    coursename=request.POST.getlist('coursename')

    #将获取到的数据插入到数据库表中
    flag=insertStu(sname,cname,coursename)

    #判断注册成功与否
    if flag:
        return HttpResponse('注册成功')
    else:
        return HttpResponse('注册失败')

#查询所有的班级信息
def showAll(request):
    clslist=Clazz.objects.all()
    return render(request,'showAll.html',{'clslist':clslist})


#查询班级下的所有学生信息
def detail(request):
    #获取请求参数
    cno=int(request.GET.get('cno','-1'))
    #通过班级表，查询学生信息
    stulist=Clazz.objects.get(cno=cno).student_set.all()

    return render(request,'detail.html',{'stulist':stulist})