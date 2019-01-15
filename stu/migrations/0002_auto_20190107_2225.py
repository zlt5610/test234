# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-07 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='spwd',
        ),
        migrations.AddField(
            model_name='student',
            name='isdelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='sname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterModelTable(
            name='student',
            table='stu4_stu4',
        ),
    ]