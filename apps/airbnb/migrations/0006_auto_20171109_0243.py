# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 02:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb', '0005_reservations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservations',
            new_name='Reservation',
        ),
    ]
