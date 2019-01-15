# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from test_AJAX_register.models import Student


class only_register(View):
    def get(self,request):
        return render(request,'only1.html')


def getInfo(request):
    #获取请求参数
    sname=request.GET.get('sname','')

    #判断
    stu=Student.objects.filter(sname=sname)
    flag=False
    if stu:
        flag=True
    return JsonResponse({'flag':flag})