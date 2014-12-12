# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientreport',
            old_name='name',
            new_name='patient_name',
        ),
        migrations.AddField(
            model_name='patientreport',
            name='picture',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
