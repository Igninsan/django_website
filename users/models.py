from django.db import models
from django.contrib.auth.models import User

first_salary = 20000
second_salary = 50000
third_salary = 100000

class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


    phone = models.CharField(max_length=14, default='+996')
    # важное для middlewares для проверки опыта работы
    experience = models.PositiveIntegerField(default=1)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    salary = models.PositiveIntegerField(max_length=8)

    def save(self, *args, **kwargs):
        if self.experience < 1:
            self.salary = 'Для получения работы нужен 1 год опыта работы'
        elif 1 <= self.experience <= 4:
            self.salary = first_salary
        elif 5 <= self.experience <= 9:
            self.salary = second_salary
        elif 10 <= self.experience <= 40:
            self.salary = third_salary
        else:
            self.ex = 'Вы слишком стары для получения этой работы'
        super().save(*args, **kwargs)