# Generated by Django 2.1.1 on 2018-10-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20181023_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='order_range',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='subsection',
            name='order_range',
            field=models.IntegerField(default=100),
        ),
    ]
