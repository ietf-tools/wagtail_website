# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_eventpagehost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventpage',
            name='host',
        ),
    ]
