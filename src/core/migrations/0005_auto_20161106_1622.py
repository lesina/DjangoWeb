# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-06 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161106_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='/home/les/Desktop/Desktop/Web/vidosso/collected_static/images/default-avatar.png', null=True, upload_to='avatars'),
        ),
    ]