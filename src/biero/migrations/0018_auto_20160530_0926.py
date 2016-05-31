# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biero', '0017_auto_20160529_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usager',
            old_name='nomUsager',
            new_name='password',
        ),
        migrations.AddField(
            model_name='usager',
            name='username',
            field=models.CharField(default=1, max_length=256, unique=True),
            preserve_default=False,
        ),
    ]