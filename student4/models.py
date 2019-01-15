# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Manager

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=30)
    isdelete=models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False):
        self.isdelete=True
        self.save()
    class Meta:
        db_table='stu4_stu4'
    def __unicode__(self):
        return u'Student:%s'%self.sname
Student.objects.all()