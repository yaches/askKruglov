# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 16:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askKruglov_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Arcticle',
            new_name='Article',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
    ]
