from django.db import models


class FeedBackModel(models.Model):
    """Обратная связь"""

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    mail = models.EmailField('Электронная почта', max_length=150)
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    name = models.CharField('Имя', max_length=50)

    def __str__(self):
        return f'{self.name} {self.mail}'
