# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    sno=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30,unique=True)

    class Meta:
        db_table='t_student'
    def __unicode__(self):
        return u'Student:%s'%self.sname
class Scard(models.Model):
    stud=models.OneToOneField(Student,primary_key=True,on_delete=models.CASCADE)
    department=models.CharField(max_length=30)
    major=models.CharField(max_length=30)
    class Meta:
        db_table='t_scard'
    def __unicode__(self):
        return u'Scard:%s'%self.major