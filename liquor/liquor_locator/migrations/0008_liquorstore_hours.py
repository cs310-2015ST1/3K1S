# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0007_auto_20150619_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquorstore',
            name='hours',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
