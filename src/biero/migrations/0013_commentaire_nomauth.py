# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biero', '0012_auto_20160526_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='nomAuth',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]