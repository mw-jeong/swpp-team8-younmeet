# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0018_auto_20171115_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='place_id',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='place',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
