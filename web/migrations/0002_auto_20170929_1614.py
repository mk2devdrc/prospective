# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='nom_categorie',
            field=models.CharField(default='Info Derniere', max_length=40),
        ),
    ]