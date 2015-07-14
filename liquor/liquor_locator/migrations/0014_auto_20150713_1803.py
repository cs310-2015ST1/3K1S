# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0013_remove_comment_objectid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liquorstore',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='liquorStore',
            field=models.ForeignKey(default=None, to='liquor_locator.LiquorStore'),
        ),
    ]
