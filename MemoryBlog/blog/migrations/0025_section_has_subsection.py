# Generated by Django 2.1.1 on 2018-11-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20181101_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='has_subsection',
            field=models.BooleanField(default=False),
        ),
    ]