# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0014_liquorstore_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='isRemoved',
            new_name='isAnon',
        ),
    ]
