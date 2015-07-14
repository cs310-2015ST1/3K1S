# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('liquor_locator', '0018_auto_20150713_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='fav_store',
        ),
        migrations.AddField(
            model_name='liquorstore',
            name='fav_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
