# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 23:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='cretaed_at',
            new_name='created_at',
        ),
    ]