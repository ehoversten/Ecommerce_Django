# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-18 01:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_1',
            new_name='address_line_1',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_2',
            new_name='address_line_2',
        ),
    ]
