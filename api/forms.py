from dataclasses import fields
from .models import Tasks, Employers
from django.forms import DateInput, DateTimeInput, ModelForm, NumberInput, TextInput, Textarea

class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['name','description','deadline','employee','progress']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задача'
            }),
             'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание задачи'
            }),
                'deadline': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дедлайн'
            }),
              'employee': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сотрудник'
            }),
               'progress': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус задачи'
            }),
        }


class EmployersForm(ModelForm):
    class Meta:
        model = Employers
        fields = ['name','age','salary','years']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя сотрудника'
            }),
             'age': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
                'salary': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Зарплата'
            }),
              'years': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стаж'
            }) 
        }