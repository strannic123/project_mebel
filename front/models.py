from django.db import models


class PartneersModel(models.Model):
    """Партнеры"""

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    name = models.CharField('Имя/Название', max_length=100)
    logo = models.ImageField('Лого', blank=True)
    created_at = models.DateField('Дата создания', auto_now=True)

    def __str__(self):
        return self.name


class VeneerModel(models.Model):
    class Meta:
        verbose_name = 'Шпон'
        verbose_name_plural = 'Шпон'
    name = models.CharField('Название', max_length=100)
    discriptions = models.CharField('Описание', max_length=1000)
    image = models.ImageField('Изображение', blank=True)
    alt = models.CharField(max_length=100, blank=True)
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title
