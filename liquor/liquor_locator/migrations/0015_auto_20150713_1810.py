# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0014_auto_20150713_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='liquorStore',
            field=models.ForeignKey(to='liquor_locator.LiquorStore', blank=True),
        ),
    ]
