# Generated by Django 2.0.3 on 2018-04-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0016_tenders_etp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenders',
            name='document_links',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Тендерные документы'),
        ),
    ]
