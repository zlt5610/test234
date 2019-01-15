# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self,request):
        return HttpResponse('hello Get请求')
    def post(self,request):
        return HttpResponse('hello Post请求')