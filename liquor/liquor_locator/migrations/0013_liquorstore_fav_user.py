# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('liquor_locator', '0012_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquorstore',
            name='fav_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
