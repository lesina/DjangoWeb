# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-06 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0009_auto_20161106_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='poster',
            field=models.FileField(null=True, upload_to='video/posters/'),
        ),
    ]
