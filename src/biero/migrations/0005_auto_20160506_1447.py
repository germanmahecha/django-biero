# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 18:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biero', '0004_auto_20160506_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biere',
            old_name='nom',
            new_name='nomBiere',
        ),
        migrations.RenameField(
            model_name='usager',
            old_name='nom',
            new_name='nomUsager',
        ),
    ]
