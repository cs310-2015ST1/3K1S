# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0013_auto_20150713_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liquorstore',
            name='fav_user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favorite',
            field=models.ManyToManyField(default=None, to='liquor_locator.LiquorStore'),
        ),
    ]
