# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
