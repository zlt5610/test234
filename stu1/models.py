# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Goods(models.Model):
    goodsid=models.AutoField(primary_key=True)
    gname=models.CharField(max_length=30)
    gdesc=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    count=models.PositiveIntegerField()
    created=models.DateField(auto_now_add=True)
    modified=models.DateField(auto_now_add=True)
    gimage=models.ImageField(upload_to='images/')

class Clazz(models.Model):
    cno=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=30,unique=30)

    class Meta:
        db_table='zlt_cls'
    def __unicode__(self):
        return u'Clazz:%s'%self.cname

class Student(models.Model):
    sno=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    cls=models.ForeignKey(Clazz)
    class Meta:
        db_table='zlt_stu2'
    def __unicode__(self):
        return u'Student:%s'%self.sname