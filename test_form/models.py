# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clazz(models.Model):
    cno=models.AutoField(primary_key=True)
    cname=models.CharField(verbose_name=u'班级名称',max_length=30,unique=True)
    def __unicode__(self):
        return r'Class:%s'%self.cname
    class Meta:
        db_table='form_Class1'

class Student(models.Model):
    sno=models.AutoField(primary_key=True)
    sname=models.CharField(verbose_name=u'学生名称',max_length=30,unique=True)
    cls=models.ForeignKey(Clazz)

    def __unicode__(self):
        return r'Student:%s'%self.sname