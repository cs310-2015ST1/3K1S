# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0006_auto_20150613_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquorstore',
            name='address',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='liquorstore',
            name='name',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
