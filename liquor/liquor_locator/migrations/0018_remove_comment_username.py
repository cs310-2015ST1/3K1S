# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0017_auto_20150713_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
    ]
