# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-03 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='client_secret',
            field=models.CharField(max_length=100),
        ),
    ]