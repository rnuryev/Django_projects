# Generated by Django 2.0.7 on 2018-07-14 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animator',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='animator',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='animator',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Персонаж'),
        ),
        migrations.AlterField(
            model_name='animator',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='std_animators', to='catalog.Studio', verbose_name='Студия'),
        ),
        migrations.AlterField(
            model_name='company',
            name='adress',
            field=models.CharField(blank=True, max_length=250, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='company',
            name='district',
            field=models.CharField(blank=True, max_length=250, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='company',
            name='site',
            field=models.CharField(blank=True, max_length=250, verbose_name='Сайт'),
        ),
        migrations.AlterField(
            model_name='school',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='schoolprogram',
            name='cost_abonement',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость Абонемента'),
        ),
        migrations.AlterField(
            model_name='schoolprogram',
            name='cost_one',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость 1 занятия'),
        ),
        migrations.AlterField(
            model_name='schoolprogram',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='schoolprogram',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='schoolprogram',
            name='schedule',
            field=models.TextField(verbose_name='Расписание'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='aria',
            field=models.FloatField(verbose_name='Площадь'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='other_condition',
            field=models.TextField(verbose_name='Прочие условия'),
        ),
    ]