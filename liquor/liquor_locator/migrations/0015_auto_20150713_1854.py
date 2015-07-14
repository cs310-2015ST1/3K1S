# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0014_auto_20150713_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favorite',
            field=models.ManyToManyField(related_name='+', to='liquor_locator.LiquorStore'),
        ),
    ]
