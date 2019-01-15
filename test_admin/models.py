# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clazz(models.Model):
    cno=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=30,unique=True,verbose_name=u'班级名称')

    def __unicode__(self):
        return u'Class:%s'%self.cname
    class Meta:
        db_table='admin_class'
        verbose_name_plural=u'班级表'

class Student(models.Model):
    sno=models.AutoField(primary_key=True,verbose_name=u'学号')
    sname=models.CharField(max_length=30,verbose_name=u'姓名')
    cls=models.ForeignKey(Clazz,verbose_name=u'所属班级')

    def __unicode__(self):
        return u'Student:%s'%self.sname
    class Meta:
        db_table='admin_student'
        verbose_name_plural=u'学生表'
