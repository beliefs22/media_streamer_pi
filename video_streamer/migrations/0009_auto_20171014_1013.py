# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_streamer', '0008_auto_20171014_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='vid',
        ),
        migrations.AlterField(
            model_name='video',
            name='video_title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]