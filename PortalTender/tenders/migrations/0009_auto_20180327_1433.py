# Generated by Django 2.0.3 on 2018-03-27 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0008_auto_20180327_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rzdtenders',
            name='bid_deadlin_from',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
