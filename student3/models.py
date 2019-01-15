# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=30)
    class Meta:
        db_table='zlt_course'
    def __unicode__(self):
        return u'Course:%s'%self.course_name
class Student(models.Model):
    sno=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    course=models.ManyToManyField(Course)
    class Meta:
        db_table='zlt_student3'
    def __unicode__(self):
        return u'Student:%s'%self.sname

