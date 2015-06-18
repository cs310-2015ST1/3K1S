# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0007_liquorstore_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquorstore',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
