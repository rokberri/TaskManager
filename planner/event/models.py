import os

import django.utils.timezone
from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField('Название события', max_length=500)
    date = models.DateField('Дата', default=django.utils.timezone.now, blank=True)
    description = models.CharField('Описание события', max_length=500)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.title


class Day(models.Model):
    events = list()
    date = models.DateField('Дата', default=django.utils.timezone.now, blank=True)

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'

    # def Day(self, day, *event):
    #     self.date = day
    #     for item in event:
    #         self.events.append(item)

    def __str__(self):
        return str(self.date)
