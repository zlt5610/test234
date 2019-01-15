# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def query_view(request):
    return HttpResponse('Hello,url!')


def query_view2(request,num1,num2):
    return HttpResponse('%s,%s'%(num1,num2))


def query_view3(request,uname,pwd):
    return HttpResponse('%s,%s'%(uname,pwd))


def query_view4(request,hello):
    return HttpResponse(hello)


def query_view5(request):
    return HttpResponse('query5展示')


def query_view6(request):
    #return HttpResponseRedirect(reverse('query5'))
    return render(request,'query6.html')