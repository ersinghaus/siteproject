# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20161202_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='file', max_length=25),
        ),
    ]