# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_bank', '0004_accounts_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='balance',
            field=models.IntegerField(default=1000),
        ),
    ]
