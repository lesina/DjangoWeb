# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(default=0, max_length=255),
        ),
    ]
