from django.db import models

class Product(models.Model):
    name = models.CharField('Название', max_length=30)
    statistical_weight = models.CharField('Склад', max_length=300)
    first_date = models.DateTimeField('Дата изготовления')
    expiration_date = models.DateTimeField('Дата окончания')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
