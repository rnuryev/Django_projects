# Generated by Django 2.0.7 on 2018-07-29 17:20

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_articlestatistic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('content', models.TextField(verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата комментария')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Article')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]