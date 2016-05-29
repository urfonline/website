# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticsSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ga_property_id', models.CharField(help_text='UA-XXXXX-X', max_length=20)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]