# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-02 13:40
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20181002_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]
