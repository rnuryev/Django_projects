from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Tenders(models.Model):
    etp = models.CharField(max_length=10, verbose_name=u'Торговая площадка', null=True, blank=True)
    code = models.CharField(max_length=100, verbose_name=u'Код тендера', null=True, blank=True)
    subject = models.CharField(max_length=2500, verbose_name=u'Предмет', null=True, blank=True)
    customer = models.CharField(max_length=250, verbose_name=u'Заказчик', null=True, blank=True)
    price = models.CharField(max_length=250, verbose_name=u'Цена', null=True, blank=True)
    deadline = models.DateField(verbose_name=u'Срок подачи заявок', null=True, blank=True)
    link = models.URLField(verbose_name=u'Ссылка', null=True, blank=True)
    lots = JSONField(null=True)
    document_links = JSONField(null=True)
    in_favorite = models.BooleanField(default=False)

    def __str__(self):
        return 'Тендер №:' + self.code


    class Meta:
        verbose_name = 'Тендер'
        verbose_name_plural = 'Тендеры'

class FavoriteTenders(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT)
    fav_tender = models.ForeignKey(Tenders, verbose_name='Избранный тендер', on_delete=models.PROTECT)

    def __str__(self):
        return 'Избранное ' + self.user.username + '. Тендер № ' + self.fav_tender.code

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'