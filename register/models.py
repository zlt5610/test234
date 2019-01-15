# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clazz(models.Model):
    cno=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=30)
    class Meta:
        db_table='register_Clazz'
    def __unicode__(self):
        return u'Class:%s'%self.cname
class Course(models.Model):
    couesr_id=models.AutoField(primary_key=True)
    coursename=models.CharField(max_length=30)
    class Meta:
        db_table='register_Course'
    def __unicode__(self):
        return u'Course:%s'%self.coursename

class Student(models.Model):
    sno=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    cls=models.ForeignKey(Clazz)
    course=models.ManyToManyField(Course)
    class Meta:
        db_table='register_student'
    def __unicode__(self):
        return u'Student:%s'%self.sname

def insertStu(sname,cname,coursenames):
    #完成注册功能的核心
    try:
        #插入班级表的数据
        try:
            cls=Clazz.objects.get(cname=cname)
        except Clazz.DoesNotExist:
            cls=Clazz.objects.create(cname=cname)
        #插入学生表的数据
        try:
            stu=Student.objects.get(sname=sname)
        except Student.DoesNotExist:
            stu=Student.objects.create(sname=sname,cls=cls)

        #插入课程表数据
        courselist=[]
        for cn in coursenames:
            try:
                course=Course.objects.get(coursename=cn)
            except Course.DoesNotExist:
                course=Course.objects.create(coursename=cn)
            courselist.append(course)

        #插入学生和课程的中间表数据
        stu.course.add(*courselist)
        return True
    except:
        return False

