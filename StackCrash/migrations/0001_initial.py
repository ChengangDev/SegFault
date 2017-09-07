# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date visited')),
                ('url', models.CharField(max_length=2048)),
                ('title', models.CharField(max_length=1024)),
                ('time', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]