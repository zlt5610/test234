# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='GET':
        return render(request,'LOGIN_login1.html')
    else:
        #获取请求参数
        uname=request.POST.get('uname','')
        pwd=request.POST.get('pwd','')
        #判断用户名登陆是否成功
        if uname=='zhangsan' and pwd=='123':
            #重定向方式1
            #return HttpResponseRedirect('https://www.baidu.com')
            # 重定向方式2
            #return redirect('https://www.taobao.com')
            # 重定向方式3
            resp=HttpResponse()
            resp.status_code=302
            resp.setdefault('Location','https://www.jd.com')
            return resp
    return HttpResponseRedirect('/LOGIN/login/')