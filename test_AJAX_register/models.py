# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=30)

    def __unicode__(self):
        return self.sname