# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StackCrash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
