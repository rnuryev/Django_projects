from django.db import models
from datetime import datetime
# Create your models here.

class NewsUser(models.Model):
    email = models.EmailField('Почта')
    user_hash = models.CharField('Код подписчика', max_length=30)
    is_active = models.BooleanField('Подписка активна', default=True)
    date_added = models.DateField('Дата подписки', default=datetime.now)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

        def __str__(self):
            return self.email