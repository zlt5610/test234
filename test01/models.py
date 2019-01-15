# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clazz(models.Model):
    cno=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=30)

class Student(models.Model):
    sno=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    score=models.DecimalField(max_digits=4,decimal_places=1)
    cls=models.ForeignKey(Clazz)
    def __unicode__(self):
        return u'Student:%s'%self.sname