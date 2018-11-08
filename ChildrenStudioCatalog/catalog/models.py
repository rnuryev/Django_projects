from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    adress = models.CharField(max_length=250, blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='Почта')
    site = models.CharField(max_length=250, blank=True, verbose_name='Сайт')
    description = models.TextField(blank=True, verbose_name='Описание')
    district = models.CharField(max_length=250, blank=True, verbose_name='Район')

    is_school = models.BooleanField(default=False, verbose_name='Является школой')
    school_desctiption = models.TextField(verbose_name='Описание школы', blank=True)

    is_studio = models.BooleanField(default=False, verbose_name='Является студией')
    studio_aria = models.FloatField(verbose_name='Площадь студии', default=0)
    studio_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость аренды', blank=True, default=0)
    own_animators = models.BooleanField(default=False, verbose_name='Есть свои аниматоры')
    studio_condition = models.TextField(verbose_name='Прочие условия (студия)', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Animator(models.Model):
    name = models.CharField(max_length=250, verbose_name='Персонаж')
    cost = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Стоимость')
    description = models.TextField(verbose_name='Описание')
    studio = models.ForeignKey(Company, related_name='std_animators', on_delete=models.CASCADE, verbose_name='Студия')

    def __str__(self):
        return self.name + '. Студия ' + self.studio.company.name

    class Meta:
        verbose_name = 'Аниматор'
        verbose_name_plural = 'Анимторы'


class SchoolProgram(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    cost_one = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость 1 занятия')
    cost_abonement = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость Абонемента')
    schedule = models.TextField(verbose_name='Расписание')
    school = models.ForeignKey(Company, verbose_name='Школа', related_name='sch_programs', on_delete=models.CASCADE)

    def __str__(self):
        return 'Программа ' + self.name + 'компании ' + self.school.company.name

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'