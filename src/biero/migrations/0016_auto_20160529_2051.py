# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biero', '0015_auto_20160529_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biere',
            name='image',
            field=models.ImageField(default='bieres/defaut.jpg', upload_to='bieres/'),
        ),
    ]
