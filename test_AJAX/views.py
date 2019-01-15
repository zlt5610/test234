# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
import time
# Create your views here.
def index_view(request):
    return render(request,'index_Ajax.html')


def get_view(request):
    uname=request.GET.get('uname','Hello')
    print uname
    time.sleep(10)
    return JsonResponse({'flag':True})


def post_view(request):
    uname = request.POST.get('uname', 'Hello')
    print uname
    return JsonResponse({'flag': False})


def custom_view(request):
    uname = request.POST.get('uname', 'Hello')
    print uname
    time.sleep(5)
    return JsonResponse({'flag': False})