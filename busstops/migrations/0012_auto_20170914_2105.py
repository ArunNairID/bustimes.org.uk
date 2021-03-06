# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 20:05
from __future__ import unicode_literals

import autoslug.fields
import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busstops', '0011_auto_20170817_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='geometry',
            field=django.contrib.gis.db.models.fields.MultiLineStringField(editable=False, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=True, populate_from='description'),
        ),
    ]
