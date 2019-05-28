# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-10-20 10:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20180928_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='percent_read',
            field=models.ManyToManyField(blank=True, related_name='percent_read', to=settings.AUTH_USER_MODEL),
        ),
    ]
