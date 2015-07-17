# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0015_auto_20150715_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='isAnon',
            new_name='isAnonymous',
        ),
    ]
