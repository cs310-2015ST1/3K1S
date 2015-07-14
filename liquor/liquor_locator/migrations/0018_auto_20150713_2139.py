# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0017_auto_20150713_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='favorites',
            new_name='fav_store',
        ),
    ]
