# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0005_liquorstore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquorstore',
            name='name',
            field=models.CharField(default=b'NA', max_length=128),
        ),
    ]
