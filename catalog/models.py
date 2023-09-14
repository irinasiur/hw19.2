from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    purchase_price = models.FloatField(verbose_name='цена за покупку')
    date_of_creation = models.DateField(auto_now_add=True, verbose_name="дата создания")
    last_modified_date = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='user')

    def __str__(self):
        nl = '\n'
        return f'{self.name}{self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Version(models.Model):
    number_of_version = models.IntegerField(default=0, verbose_name='номер версии')
    label = models.CharField(max_length=100, verbose_name='название версии', db_column='name')
    is_active = models.BooleanField(verbose_name='признак текущей версии', default=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return f"{self.product} {self.name} "

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
