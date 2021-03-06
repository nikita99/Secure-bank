# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_bis1', '0004_auto_20160410_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=25)),
                ('amount_paid', models.IntegerField(default=0, max_length=30)),
                ('item_price', models.IntegerField(default=100)),
                ('license_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_bis1.Signup')),
            ],
        ),
    ]
