# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class TMovie(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    account = models.CharField(max_length=500, blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)
    download_url = models.CharField(max_length=300, blank=True, null=True)
    def __unicode__(self):
        return u'TMovie:%s'% self.name
    class Meta:
        managed = False
        db_table = 't_movie'
