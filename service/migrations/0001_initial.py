# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientReport',
            fields=[
                ('i_patient_report', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'Username')),
                ('ic', models.CharField(max_length=128, verbose_name=b'Identity')),
                ('gender', models.CharField(max_length=1, verbose_name=b'Gender', choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')])),
                ('emergency_type', models.CharField(max_length=2, choices=[(b'ha', b'Heart Attack'), (b'as', b'Asthma'), (b'ac', b'Accident'), (b'tr', b'Trauma'), (b'po', b'Poisonous'), (b'bl', b'Bleeding'), (b'ch', b'Choke'), (b'bt', b'Bitten')])),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'patient_report',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('i_staff', models.AutoField(serialize=False, primary_key=True)),
                ('staff_username', models.CharField(max_length=128, verbose_name=b'Username')),
                ('staff_password', models.CharField(max_length=128, verbose_name=b'Password')),
            ],
            options={
                'db_table': 'staff',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patientreport',
            name='reported_by',
            field=models.ForeignKey(to='service.Staff'),
            preserve_default=True,
        ),
    ]
