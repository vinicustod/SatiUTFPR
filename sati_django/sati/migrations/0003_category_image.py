# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sati', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=None, upload_to=b''),
        ),
    ]