# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busstops', '0002_service_show_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='line_ver',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]