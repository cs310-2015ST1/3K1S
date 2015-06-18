# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0008_auto_20150617_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquorstore',
            name='address',
            field=models.CharField(max_length=128),
        ),
    ]
