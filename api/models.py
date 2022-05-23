from django.db import models
from simple_history.models import HistoricalRecords

class Tasks(models.Model):
    name = models.CharField('Задача', max_length=25)
    description = models.TextField('Описание задачи')
    deadline = models.DateTimeField('Дедлайн')
    employee = models.CharField('Сотрудник', max_length=30)
    progress = models.CharField('Статус задачи', max_length=30)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Employers(models.Model):
    name = models.CharField('Имя', max_length=25)
    age = models.IntegerField('Возраст')
    salary = models.IntegerField('Зарплата')
    years = models.CharField('Стаж', max_length=50)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
