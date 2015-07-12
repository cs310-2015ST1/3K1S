# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0008_liquorstore_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquorstore',
            name='storeHash',
            field=models.CharField(max_length=32, blank=True),
        ),
    ]
