# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Area(models.Model):
    areaid=models.IntegerField(primary_key=True)
    areaname=models.CharField(max_length=50)
    parentid=models.IntegerField()
    arealevel=models.IntegerField()
    status=models.IntegerField()

    class Meta:
        #managed=False
        db_table='area'