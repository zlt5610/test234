# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from .forms import *
from django.contrib.auth import *


class LoginView(View):
    def get(self,request):
        login_form=LoginForm()
        return render(request,'form_login.html',{'login_form':login_form})
    def post(self,request):
        login_form=LoginForm(request.POST)
        #表单校验
        if login_form.is_valid():
            data=login_form.cleaned_data
            print data
            #根据用户输入的用户名和密码取系统数据库中进行查询是否存在
            user=authenticate(username=data['username'],password=data['password'])

            if user:
                login(request,user)
                return HttpResponse('登陆成功')
            else:
                return render(request,'form_login.html',{'login_form':login_form})


class RegisterView(View):
    def get(self,request):
        #创建表单类对象
        cls_Form=ClazzForm
        stu_Form=StudentForm

        return render(request,'form_register.html',{'cls_Form':cls_Form,'stu_Form':stu_Form})
    def post(self,request):
        cls_Form=ClazzForm(request.POST)
        stu_Form=StudentForm(request.POST)

        #表单校验
        if cls_Form.is_valid()*stu_Form.is_valid():
            cls=cls_Form.save(commit=True)
            stu=stu_Form.save(commit=False)
            stu.cls=cls
            stu.save()
            return HttpResponse('注册成功')
        else:
            return render(request, 'form_register.html', {'cls_Form': cls_Form, 'stu_Form': stu_Form})
