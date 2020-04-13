from django.db import models


class CategoryModel(models.Model):
    """Категории"""

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Название', max_length=150)
    h1 = models.CharField('Заголовок SEO', max_length=50)
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('url', unique=True)
    descriptions = models.CharField('Описание', max_length=1000)
    position = models.IntegerField('Позиция')
    enabled = models.BooleanField('Отображать категорию ?')
    text = models.TextField('Текст', blank=True, default=True)
    image_menu = models.ImageField('Изображение', blank=True, default=True)
    image = models.ImageField('Изображение', blank=True, default=True)
    show_main = models.BooleanField('Отображать ?')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now_add=True)

    def __str__(self):
        return self.name


class PostModel(models.Model):
    class Meta:
        verbose_name = 'Пост'

    category = models.ForeignKey(CategoryModel, verbose_name='Категории', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('url', unique=True)
    title = models.CharField('Заголовок', max_length=100)
    description = models.CharField('Описание', max_length=1000)
    text = models.TextField('Текст')
    enabled = models.BooleanField('Опубликовать ?', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PostImageModel(models.Model):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    image = models.ImageField('Изображение', blank=True)
    alt = models.CharField('Описание SEO', max_length=50)
    title = models.ForeignKey(CategoryModel, verbose_name='Название', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
