# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sati', '0008_person_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=32),
        ),
    ]
