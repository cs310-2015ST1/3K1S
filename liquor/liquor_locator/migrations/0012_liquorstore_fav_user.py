# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0011_auto_20150712_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquorstore',
            name='fav_user',
            field=models.ManyToManyField(to='liquor_locator.UserProfile'),
        ),
    ]
