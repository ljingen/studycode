# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 11:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170728_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 11, 23, 23, 39895), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 11, 23, 23, 39920), verbose_name='修改时间'),
        ),
    ]