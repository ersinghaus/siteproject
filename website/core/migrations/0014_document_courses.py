# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_document_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='courses',
            field=models.CharField(choices=[('Math', 'math'), ('Art', 'art')], default=('Math', 'math'), max_length=25),
        ),
    ]
