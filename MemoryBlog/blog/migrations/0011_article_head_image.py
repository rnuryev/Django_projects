# Generated by Django 2.0.7 on 2018-07-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_article_head_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='head_image',
            field=models.ImageField(default='post_images/None/default_image_to_post.jpg', null=True, upload_to='post_images/'),
        ),
    ]
