# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='docfile',
            new_name='imgfile',
        ),
    ]