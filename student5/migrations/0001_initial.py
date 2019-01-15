# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-07 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clazz',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'student5_class',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseno', models.AutoField(primary_key=True, serialize=False)),
                ('coursename', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'student5_course',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30)),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student5.Clazz')),
                ('course', models.ManyToManyField(to='student5.Course')),
            ],
            options={
                'db_table': 'student5_student',
            },
        ),
    ]