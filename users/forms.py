from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER  = (
    ('M', 'Male'),
    ('F', 'Female'),
    )

class CustomRegisterForm(UserCreationForm):
    phone_number = forms.CharField(required=True, label='Укажите ваш номер телефона')
    email = forms.EmailField(required=True, label='Введите ваш Email')
    first_name = forms.CharField(required=True, label='Укажите ваше имя')
    surname = forms.CharField(required=True, label='Укажите вашу фамилию')
    city = forms.CharField(required=True, label='Укажите город, в котором вы проживаете')
    age = forms.IntegerField(required=True, label='Укажите ваш возраст')
    reason = forms.CharField(required=True, label='Укажите причину, по которой вы хотите устроиться на эту работу')
    gender = forms.ChoiceField(choices=GENDER, label='Укажите ваш пол')
    experience = forms.IntegerField(required=True, label='Укажите ваш опыт работы')
    education_level = forms.CharField(required=True, label='Укажите ваш уровень образования')


    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'surname',
            'city',
            'age',
            'reason',
            'gender',
            'phone_number',
            'education_level',
            'experience',
        )
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.surname = self.cleaned_data['surname']
        user.city = self.cleaned_data['city']
        user.age = self.cleaned_data['age']
        user.reason = self.cleaned_data['reason']
        user.phone_number = self.cleaned_data['phone_number']
        user.gender = self.cleaned_data['gender']
        user.experience = self.cleaned_data['experience']
        user.education_level = self.cleaned_data['education_level']

        if commit:
            user.save()

        return user