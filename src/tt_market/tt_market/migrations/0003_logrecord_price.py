# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-18 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_market', '0002_auto_20170818_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='logrecord',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]