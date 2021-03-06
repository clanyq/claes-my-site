# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedapp', '0002_auto_20161207_0923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='press',
            options={'verbose_name_plural': 'Press'},
        ),
        migrations.AddField(
            model_name='image',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default='360', editable=False, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, default='480', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='pubdate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='press',
            name='pubdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
