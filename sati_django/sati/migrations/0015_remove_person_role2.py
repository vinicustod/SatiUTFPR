# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 03:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sati', '0014_person_role2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='role2',
        ),
    ]