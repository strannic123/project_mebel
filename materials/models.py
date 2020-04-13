from django.db import models


class MaterialsModel(models.Model):
    """Материалы"""
    name = models.CharField('Название', max_length=100)
    text = models.TextField('Текст')
    created_at = models.DateTimeField(auto_now_add=True)


class MaterialImagesModel(models.Model):
    """Описание материалов"""
    image = models.ImageField('Изображение', blank=True)
    material = models.ForeignKey(MaterialsModel, verbose_name='Id материала', on_delete=models.CASCADE)
    alt = models.CharField('Описание SEO', max_length=50)
    title = models.CharField('Название', max_length=100)


