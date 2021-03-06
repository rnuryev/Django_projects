# Generated by Django 2.1.1 on 2018-10-26 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsuser',
            name='date_added',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата подписки'),
        ),
        migrations.AlterField(
            model_name='newsuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='newsuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Подписка активна'),
        ),
        migrations.AlterField(
            model_name='newsuser',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='newsuser',
            name='user_hash',
            field=models.CharField(max_length=30, verbose_name='Код подписчика'),
        ),
    ]
