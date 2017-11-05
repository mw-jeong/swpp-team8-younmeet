# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20171104_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email / address'),
        ),
    ]
