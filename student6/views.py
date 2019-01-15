# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from student6.models import Student
from test234.settings import MEDIA_ROOT


def upload(request):

    return render(request,'upload.html')


def toupload(request):
    #获取请求参数
    sname=request.POST.get('sname')
    photo=request.FILES.get('photo')
    #入库操作
    student=Student.objects.create(sname=sname,photo=photo)
    #判断图片是否上传成功
    if student:
        return HttpResponse('注册成功')
    else:
        return HttpResponse('注册失败')


def showall(request):
    students=Student.objects.all()
    return render(request,'showall_1.html',{'stus':students})

#起到预览效果
def download1(request):
    #images/img03.jpg
    photo=request.GET.get('photo')
    #获取flag的值
    flag=request.GET.get('flag')
    #获取文件名，rindex：从右往左数，数到第一个‘/’
    filename=photo[photo.rindex('/')+1:]
    #获取文件存储位置
    import os
    filepath=os.path.join(MEDIA_ROOT,photo)

    print filepath

    with open(filepath,'rb') as fr:
        content=fr.read()

    response=HttpResponse(content)
    response['content-type']='image/jpg'

    if flag=='2':
    #设置响应头信息，实现附件下载功能
        response['content-disposition']='attachment;filename='+filename

    return response