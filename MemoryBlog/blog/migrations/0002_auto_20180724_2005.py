# Generated by Django 2.0.7 on 2018-07-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
