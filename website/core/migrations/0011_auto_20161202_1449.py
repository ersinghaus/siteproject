# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20161202_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='Enter File Name', max_length=25),
        ),
    ]
