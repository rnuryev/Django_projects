# Generated by Django 2.0.3 on 2018-03-23 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rzdtenders',
            name='bid_deadlin_from',
            field=models.DateField(default=None),
        ),
    ]
