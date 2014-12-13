# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_patientreport_reporting_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientreport',
            name='reporting_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 16, 10, 0, 624720), verbose_name=b'Reported Time', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
