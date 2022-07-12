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
    storage = models.ForeignKey('Storage', blank=True, null=True, related_name='organizations',
                                on_delete=models.SET_NULL, verbose_name='склад')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
