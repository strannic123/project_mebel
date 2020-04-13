from django.db import models


class RewievsModel(models.Model):
    """Отзывы"""
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    name = models.CharField('Название', max_length=200)
    text = models.TextField('Текс')
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
