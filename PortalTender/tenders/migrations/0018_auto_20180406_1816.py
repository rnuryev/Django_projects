# Generated by Django 2.0.3 on 2018-04-06 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0017_auto_20180406_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenders',
            name='subject',
            field=models.CharField(blank=True, max_length=2500, null=True, verbose_name='Предмет'),
        ),
    ]
