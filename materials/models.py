from django.db import models

from catalog.models import NULLABLE


class Material(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='material', verbose_name='изображение', **NULLABLE)
    slug = models.CharField(max_length=100, null=True, blank=True, verbose_name='slug')
    publishing_flag = models.BooleanField(verbose_name='признак публикации', default=True)
    creation_date = models.DateField(auto_now_add=True, verbose_name="дата создания")
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
