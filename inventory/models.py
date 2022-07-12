from django.db import models


class Storage(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    storage = models.ManyToManyField('Storage', blank=True, related_name='organizations', verbose_name='Склады')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
