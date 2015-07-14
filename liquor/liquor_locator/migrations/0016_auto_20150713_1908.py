# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0015_auto_20150713_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favorites', models.ForeignKey(to='liquor_locator.LiquorStore', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite',
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.OneToOneField(to='liquor_locator.UserProfile'),
        ),
    ]
