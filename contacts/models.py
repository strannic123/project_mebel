from django.db import models
from solo.models import SingletonModel


class ContactsModel(SingletonModel):
    """Контакты"""
    phone = models.CharField('тел', max_length=20)
    phone_2 = models.CharField('тел_2', max_length=20)
    address = models.CharField('адрес', max_length=20)
    address_2 = models.CharField('адрес_2', max_length=20)
    email = models.EmailField('@mail', max_length=50)
    vk = models.CharField('VK', max_length=150)
    instagramm = models.CharField('Instagramm', max_length=150)
    telegramm = models.CharField('Instagramm', max_length=150)
