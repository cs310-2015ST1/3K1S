# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0005_liquorstore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liquorstore',
            name='latlon',
        ),
        migrations.AddField(
            model_name='liquorstore',
            name='lat',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AddField(
            model_name='liquorstore',
            name='lon',
            field=models.CharField(max_length=64, blank=True),
        ),
    ]
