# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 19:26
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_menu_menuitem_menusettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='server.Menu'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='menusettings',
            name='header_menu',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Menu'),
        ),
    ]