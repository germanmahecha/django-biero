# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('brasserie', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=256)),
                ('image', models.FileField(upload_to=b'')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('modifie', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Usager',
        ),
    ]
