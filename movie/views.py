# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from movie.models import TMovie
# 原生分页操作
# import math
# def page_movie(num,size=12):
#     #判断是否越界
#     if num<1:
#         num=1
#     #获取总记录数
#     totalRecords=TMovie.objects.all().count()
#     #获取总页数
#     totalPages=int(math.ceil(totalRecords*1.0/size))
#
#     if num>totalPages:
#         num=totalPages
#
#     #获取当前页的所有数据
#     mlist=TMovie.objects.all()[(num-1)*size:num*size]
#     return mlist
# def index_view(request,num=1):
#     num=int(request.GET.get('num',1))
#     #获取t_movie表中的所有数据
#     # movielist=TMovie.objects.all()
#     #分页用
#     movielist=page_movie(num)
#     previous_page=num-1
#     next_page=num+1
#     return render(request,'index01.html',{'movielist':movielist,'previous_page':previous_page,'next_page':next_page})

# django分页
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import math
def index_view(request):
    num=int(request.GET.get('num',1))
    movielist=TMovie.objects.all().order_by('id')
    #分页对象
    page_obj=Paginator(movielist,12)
    #获取当前页的数据
    try:
        per_page_list=page_obj.page(num)
    except PageNotAnInteger:
        per_page_list=page_obj.page(1)
    except EmptyPage:
        per_page_list=page_obj.page(page_obj.num_pages)

    #每页开始页码
    begin=(num-int(math.ceil(10.0/2)))
    if begin<1:
        begin=1
    #每页结束页码
    end=begin+9
    if end>page_obj.num_pages:
        end=page_obj.num_pages
    if end<=10:
        begin=1
    else:
        begin=end-9
    pagelist=range(begin,end+1)
    return render(request,'index01.html',{'movielist':per_page_list,'pagelist':pagelist,'currentNum':num,'lastpage':page_obj.num_pages})
