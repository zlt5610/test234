# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Manager


# class CustomManager(Manager):
#     def __getCls(self,cname):
#         try:
#             cls=Clazz.objects.get(cname=cname)
#         except Clazz.DoesNotExist:
#             cls=Clazz.objects.create(cname=cname)
#         return cls
#     def create(self,**kwargs):
#         #获取班级名称
#         cname=kwargs.get('cls')
#         #获取班级对象
#         cls=self.__getCls(cname)
#         #替换原先的班级名称
#         kwargs['cls']=cls
#         #移除课程名称的元组
#         course=kwargs.pop('course')
#         #插入学生表信息
#         stuobj=Manager.create(self,**kwargs)
#         #插入课程表信息
#         courselist=[]
#         for cn in course:
#             try:
#                 cour=Course.objects.get(coursename=cn)
#             except Course.DoesNotExist:
#                 cour=Course.objects.create(coursename=cn)
#             courselist.append(cour)
#         #插入中间表
#         stuobj.course.add(*courselist)
#
#         return stuobj

# Create your models here.
class Clazz(models.Model):
    cno=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=30)
    class Meta:
        db_table='student5_class'
    def __unicode__(self):
        return u'Class:%s'%self.cname

class Course(models.Model):
    courseno=models.AutoField(primary_key=True)
    coursename=models.CharField(max_length=30)
    class Meta:
        db_table='student5_course'
    def __unicode__(self):
        return u'Course:%s'%self.coursename
class Student(models.Model):
    sno=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    cls=models.ForeignKey(Clazz)
    course=models.ManyToManyField(Course)

    #objects=CustomManager()
    #from django.db.transaction import atomic
    #重写save方法
    #atomic保证事务的隔离性
   # @atomic()
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.cls=Clazz.objects.get(cname=self.cls.cname)
        except Clazz.DoesNotExist:
            self.cls=Clazz.objects.create(cname=self.cls.cname)
        #1/0
        return models.Model.save(self)
    class Meta:
        db_table='student5_student'
    def __unicode__(self):
        return u'Course:%s'%self.sname