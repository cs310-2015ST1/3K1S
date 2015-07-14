# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0012_liquorstore_fav_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquorstore',
            name='fav_user',
            field=models.ManyToManyField(default=None, to='liquor_locator.UserProfile'),
        ),
    ]
