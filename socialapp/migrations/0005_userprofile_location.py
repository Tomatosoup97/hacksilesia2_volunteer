# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0004_post_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default='katowice', max_length=100),
            preserve_default=False,
        ),
    ]
