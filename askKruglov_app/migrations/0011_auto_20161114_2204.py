# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askKruglov_app', '0010_auto_20161114_2023'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='profile',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
