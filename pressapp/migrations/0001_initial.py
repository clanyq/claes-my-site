# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-02 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('source', models.CharField(max_length=50)),
                ('pubdate', models.DateField()),
            ],
        ),
    ]
