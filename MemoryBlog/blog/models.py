from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.contrib.postgres.fields.array import ArrayField
from newsletter.models import NewsUser
from post_office import mail

# Create your models here.

class Section(models.Model):
    class Meta:
        db_table = 'section'
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    name = models.CharField(max_length=200)
    sec_slug = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    seo_desription = models.CharField(max_length=200, blank=True)
    order_range = models.IntegerField(default=100)
    has_subsection = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Subsection(models.Model):
    class Meta:
        db_table = 'subsection'
        verbose_name = 'Подраздел'
        verbose_name_plural = 'Подразделы'

    name = models.CharField(max_length=200)
    subsec_slug = models.SlugField()
    description = models.TextField(blank=True)
    seo_desription = models.CharField(max_length=200, blank=True)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    order_range = models.IntegerField(default=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Subsection, self).save(*args, **kwargs)
        subs = self.section
        if not subs.has_subsection:
            subs.has_subsection = True
            subs.save()


class Article(models.Model):
    class Meta:
        db_table = 'article'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    STATUS_CHOICE = (
        ('черновик', 'Черновик'),
        ('опубликован', 'Опубликован')
    )

    article_title = models.CharField(verbose_name='Заголовок статьи', max_length=200, default='Новая статья')
    slug = models.SlugField()
    article_description = models.TextField(max_length=200, blank=True, verbose_name='Краткое описание статьи')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Раздел')
    subsection = models.ForeignKey(Subsection, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Подраздел')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    date = models.DateTimeField(verbose_name='Дата публикации')
    head_image = models.ImageField(upload_to='post_images/', default='post_images/None/default_image.jpg', verbose_name='Изображение в шапке')
    content = RichTextUploadingField(verbose_name='Содержание поста', config_name='default')
    status = models.CharField(verbose_name='Статус', max_length=11, choices=STATUS_CHOICE, default='черновик')
    allow_comments = models.BooleanField(verbose_name='Разрешены комментарии', default=True)

    seo_desription = models.CharField(verbose_name='СЕО-описание', max_length=140, blank=True)
    seo_title = models.CharField(verbose_name='СЕО-title', max_length=90, blank=True)
    seo_keywords = models.CharField(verbose_name='СЕО-keywords', max_length=140, blank=True)

    def __str__(self):
        return self.article_title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    #Переопределение метода save() для рассылки уведомлений сразу после публикации новой статьи.
    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        if self.status == 'опубликован':
            subscribers = NewsUser.objects.all().filter(is_active=True)
            for i in subscribers:
                mail.send(
                    i.email,
                    'zoltan66@mail.ru',
                    # subject='Новая статья на "Чердаке Воспоминаний"!',
                    # message='У нас новая статья!',
                    template='new_article',
                    context={'article_title': self.article_title,
                             'article_url': 'http://127.0.0.1:8000' + self.get_absolute_url(),
                             'url_unsubscribe': 'http://127.0.0.1:8000/newsletter/unsubscribe/' + i.user_hash + '/'},
                    priority='now',
                )


class ArticleStatistic(models.Model):
    class Meta:
        db_table = 'ArticalStatistic'
        verbose_name = 'Статистика по статьям'
        verbose_name_plural = 'Статистики по статьям'

    article = models.ForeignKey(Article, verbose_name='Статья', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now, verbose_name='Дата статистики')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.article.article_title


class Comment(models.Model):
    class Meta:
        db_table = "comments"
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    path = ArrayField(models.IntegerField())
    article_id = models.ForeignKey(Article, on_delete=models.PROTECT)
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField('Комментарий')
    pub_date = models.DateTimeField('Дата комментария', default=timezone.now)

    def __str__(self):
        return self.content[0:200]

    def get_offset(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return level

    def get_col(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return 12 - level