# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='facebook_event',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook Event URL'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='ussu_event',
            field=models.URLField(blank=True, null=True, verbose_name='Students Union Event Page URL'),
        ),
    ]
