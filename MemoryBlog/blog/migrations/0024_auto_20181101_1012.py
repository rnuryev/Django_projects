# Generated by Django 2.1.1 on 2018-11-01 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20181031_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='seo_desription',
            field=models.CharField(blank=True, max_length=140, verbose_name='СЕО-описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='seo_keywords',
            field=models.CharField(blank=True, max_length=140, verbose_name='СЕО-keywords'),
        ),
        migrations.AlterField(
            model_name='article',
            name='seo_title',
            field=models.CharField(blank=True, max_length=90, verbose_name='СЕО-title'),
        ),
    ]