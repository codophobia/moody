# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-30 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20161130_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(default='null', upload_to='songs/'),
        ),
    ]