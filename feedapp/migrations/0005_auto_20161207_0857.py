# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedapp', '0004_auto_20161206_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
