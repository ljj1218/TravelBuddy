# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-26 18:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_auto_20170726_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='dateend',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='travel',
            name='datefrom',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
