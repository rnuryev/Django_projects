# Generated by Django 2.0.3 on 2018-03-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0002_auto_20180323_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rzdtenders',
            name='bid_deadlin_from',
            field=models.DateField(blank=True, default=None),
        ),
    ]
