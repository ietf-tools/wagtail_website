# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_auto_20170707_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='venue_section_title',
            field=models.CharField(blank=True, default='Meeting venue information', max_length=255),
        ),
    ]
