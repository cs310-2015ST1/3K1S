# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquor_locator', '0011_auto_20150712_0533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32)),
                ('comment', models.CharField(max_length=128)),
                ('isRemoved', models.BooleanField(default=False)),
                ('objectId', models.TextField(unique=True, max_length=32)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='liquorstore',
            name='comment',
            field=models.ForeignKey(to='liquor_locator.Comment', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='comment',
            field=models.ForeignKey(to='liquor_locator.Comment', null=True),
        ),
    ]
