# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-20 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_axf_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Axf_foodtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=10)),
                ('typename', models.CharField(max_length=20)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]