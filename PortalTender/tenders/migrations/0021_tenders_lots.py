# Generated by Django 2.0.3 on 2018-04-13 12:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0020_auto_20180411_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenders',
            name='lots',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
