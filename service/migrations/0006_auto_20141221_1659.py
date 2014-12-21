# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20141213_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientreport',
            name='emergency_type',
            field=models.CharField(max_length=2, choices=[(b'he', b'Heart Attack'), (b'as', b'Asthma'), (b'ac', b'Accident'), (b'tr', b'Trauma'), (b'po', b'Poisonous'), (b'bl', b'Bleeding'), (b'ch', b'Choke'), (b'bi', b'Bitten')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientreport',
            name='reporting_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 16, 59, 50, 859174), verbose_name=b'Reported Time', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
