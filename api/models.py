from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'категорию объявлений'
        verbose_name_plural = 'Категория объявлений'

    name = models.CharField('Название категории', max_length=128)

    def __str__(self):
        return self.name


class City(models.Model):
    class Meta:
        verbose_name = 'город объявлений'
        verbose_name_plural = 'Город объявлений'

    name = models.CharField('Название города', max_length=128)

    def __str__(self):
        return self.name


class Advert(models.Model):
    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'Объявления'

    created = models.DateTimeField('Дата создания', auto_now_add=True)
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Описание')
    city = models.ForeignKey(City, verbose_name='Город для объявления', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория объявления', on_delete=models.CASCADE)
    views = models.PositiveIntegerField('Просмотры', default=0)

