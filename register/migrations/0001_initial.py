# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-07 10:10
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
                'db_table': 'register_Clazz',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('couesr_id', models.AutoField(primary_key=True, serialize=False)),
                ('coursename', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'register_Course',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30)),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Clazz')),
                ('course', models.ManyToManyField(to='register.Course')),
            ],
            options={
                'db_table': 'register_student',
            },
        ),
    ]
