# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_video_video_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='poster',
            field=models.FileField(blank=True, null=True, upload_to='video/posters/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='video/'),
        ),
    ]
