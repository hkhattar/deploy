# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0005_auto_20161018_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
