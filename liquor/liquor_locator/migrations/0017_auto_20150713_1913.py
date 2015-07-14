# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0016_auto_20150713_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='favorites',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favorites',
            field=models.ForeignKey(to='liquor_locator.LiquorStore', null=True),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
