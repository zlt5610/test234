# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=30,unique=True)
    photo=models.ImageField(upload_to='images/student6/')