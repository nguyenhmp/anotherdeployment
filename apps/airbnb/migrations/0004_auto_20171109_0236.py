# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb', '0003_rental'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to='airbnb.User'),
        ),
    ]
