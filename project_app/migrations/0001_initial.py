# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('technology_used', models.CharField(max_length=150, null=True, blank=True)),
                ('cost_per_hour', models.DecimalField(default=Decimal('0.00'), max_digits=8, decimal_places=2)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('time_spent', models.IntegerField(help_text=b'Time Spent in Hours', null=True, blank=True)),
                ('client', models.ForeignKey(to='client_app.Client')),
            ],
        ),
    ]
