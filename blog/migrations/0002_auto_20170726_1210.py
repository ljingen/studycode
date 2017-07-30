# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 12:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 26, 12, 10, 16, 352002), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 26, 12, 10, 16, 352028), verbose_name='修改时间'),
        ),
    ]