# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180330_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='desc',
            old_name='context',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='desc',
            name='course',
        ),
        migrations.RemoveField(
            model_name='desc',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='desc',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='course',
            name='desc',
            field=models.OneToOneField(default='laskdjflsdjfsl', on_delete=django.db.models.deletion.CASCADE, to='app1.Desc'),
            preserve_default=False,
        ),
    ]
