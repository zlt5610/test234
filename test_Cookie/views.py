# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def set_CookieInfo(request):
    #在Cookie中存值
    respone=HttpResponse()
    #默认情况下，Cookie保存在浏览器的缓存中
    #当设置了有效时长后，数据会保存到硬盘中
    #respone.set_cookie('uname','zhangsan',max_age=1*24*60*60,path='/test_Cookie/abc/')
    a='hello'
    b=base64.encodestring(a)
    respone.set_signed_cookie('uname',b,salt='hello',path='/test_Cookie/abc/')
    return respone


def get_CookieInfo(request):
    c=request.get_signed_cookie('uname',salt='hello')
    uname=base64.decodestring(c)
    #print request.COOKIES
    return HttpResponse('value:%s'%uname)


def login_view(request):
    #读取Cookie中保存的正确的用户名和密码
    if request.COOKIES.has_key('user'):
        #获取字符串‘zhangsan，123’
        user=request.COOKIES.get('user')
        us=user.split(',')
        uname=us[0]
        pwd=us[1]
        return render(request,'Cookie_login.html',{'uname':uname,'pwd':pwd})
    return render(request,'Cookie_login.html')


def tologin_view(request):
    #获取请求参数
    uname=request.POST.get('uname','')
    pwd=request.POST.get('pwd','')
    flag=request.POST.get('flag','')

    resp=HttpResponse()
    #判断是否登陆成功
    if uname=='zhangsan' and pwd=='123':
        resp.content=u'登陆成功！'
        if flag=='1':
            resp.set_signed_cookie('user',uname+','+pwd,max_age=3*24*60*60,path='/test_Cookie/login')
            return resp
        else:
            resp.delete_cookie('user',path='/test_Cookie/login')
            return resp
    else:
        resp.delete_cookie('user', path='/test_Cookie/login')
        resp.status_code=302
        resp.setdefault('Location','/test_Cookie/login')
    return resp


def set_Session(request):
    request.session['uname']='zhangsan'
    request.session.set_expiry(5)
    return HttpResponse('Hello')


def get_Session(request):
    uname=request.session.get('uname','')

    return HttpResponse(uname)

class User(object):
    def __init__(self,uname,pwd):
        self.uname=uname
        self.pwd=pwd
import jsonpickle
def login1_view(request):
    if request.method=='GET':
        return render(request,'Cookie_login1.html')
    else:
        #获取请求参数
        uname=request.POST.get('uname','')
        pwd=request.POST.get('pwd','')
        #判断是否登陆成功
        if uname=='zhangsan' and pwd=='123':
            user=User(uname,pwd)
            request.session['user']=jsonpickle.dumps(user)

            return redirect('/test_Cookie/main/')
        else:
            return redirect('/test_Cookie/login1/')



def main(request):
    #从session中获取用户名
    user=request.session.get('user','')
    if user:
        u=jsonpickle.loads(user)
    uname=u.uname

    return HttpResponse(u'欢迎%s登陆成功'%uname)