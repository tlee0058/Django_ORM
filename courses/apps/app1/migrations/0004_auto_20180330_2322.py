# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20180330_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='desc',
        ),
        migrations.AddField(
            model_name='course',
            name='desc',
            field=models.ManyToManyField(to='app1.Desc'),
        ),
    ]