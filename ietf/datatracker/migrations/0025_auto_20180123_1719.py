# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-23 17:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datatracker', '0024_auto_20170705_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='updating',
        ),
        migrations.RemoveField(
            model_name='charter',
            name='updating',
        ),
        migrations.RemoveField(
            model_name='email',
            name='updating',
        ),
        migrations.RemoveField(
            model_name='internetdraft',
            name='updating',
        ),
        migrations.RemoveField(
            model_name='person',
            name='updating',
        ),
        migrations.RemoveField(
            model_name='rfc',
            name='updating',
        ),
        migrations.RemoveField(
            model_name='role',
            name='updating',
        ),
        migrations.RemoveField(
            model_name='rolename',
            name='updating',
        ),
        migrations.RemoveField(
            model_name='workinggroup',
            name='updating',
        ),
    ]
