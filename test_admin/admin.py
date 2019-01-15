# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from test_admin.models import Student, Clazz

class StudentAdmin(admin.ModelAdmin):
    list_display = ['sno','sname']
    list_filter = ['sno']
    search_fields = ['sno','sname']
    raw_id_fields = ['cls']
    ordering = ['sno']

admin.site.register(Clazz)
admin.site.register(Student,StudentAdmin)
