# Generated by Django 2.0.3 on 2018-03-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0005_auto_20180323_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rzdtenders',
            name='bid_deadlin_from',
            field=models.CharField(max_length=50),
        ),
    ]
