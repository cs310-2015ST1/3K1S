# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0013_liquorstore_fav_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquorstore',
            name='phone',
            field=models.CharField(max_length=32, blank=True),
        ),
    ]
