from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Client

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Придумайте логин'}))
    password1 = forms.CharField(label="Пароль" , widget=forms.PasswordInput(attrs={'class': 'formInput', 'placeholder': 'Придумайте пароль'}))
    password2 = forms.CharField(label="Повтор пароля",  widget=forms.PasswordInput(attrs={'class': 'formInput', 'placeholder': 'Повторите пароль'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# - Login a user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Введите логин'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'formInput', 'placeholder': 'Введите пароль'}))

# - Create Clients

class CreateClientForm(forms.ModelForm):
    Lname = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Введите фамилию клиента'}))
    Fname = forms.CharField(label="Имя" , widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Введите имя клиента'}))
    Mname = forms.CharField(label="Отчество",  widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Введите отчество клиента'}))
    email = forms.CharField(label="Почта", widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Укажите почту клиента'}))
    phone = forms.CharField(label="Номер телефона", widget=forms.TextInput(attrs={'class': 'formInput','placeholder': 'Укажите номер телефона клиента'}))
    birthday = forms.CharField(label="Дата рождения", widget=forms.TextInput(attrs={'class': 'formInput', 'type': 'date' , 'placeholder': 'Укажите дату рождения клиента'}))
    group = forms.CharField(label="Категория клиента", widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Укажите категорию'}))
    country = forms.CharField(label="Страна", widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Страна клиента'}))
    class Meta:
        model = Client
        fields = ['Lname', 'Fname', 'Mname', 'email', 'phone', 'birthday', 'group', 'country' ]

# - Update Clients

class UpdateClientForm(forms.ModelForm):
    Lname = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Введите фамилию клиента'}))
    Fname = forms.CharField(label="Имя" , widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Введите имя клиента'}))
    Mname = forms.CharField(label="Отчество",  widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Введите отчество клиента'}))
    email = forms.CharField(label="Почта", widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Укажите почту клиента'}))
    phone = forms.CharField(label="Номер телефона", widget=forms.TextInput(attrs={'class': 'formInput','placeholder': 'Укажите номер телефона клиента'}))
    birthday = forms.CharField(label="Дата рождения", widget=forms.TextInput(attrs={'class': 'formInput', 'type': 'date' , 'placeholder': 'Укажите дату рождения клиента'}))
    group = forms.CharField(label="Категория клиента", widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Укажите категорию'}))
    country = forms.CharField(label="Страна", widget=forms.TextInput(attrs={'class': 'formInput', 'placeholder': 'Страна клиента'}))
    class Meta:
        model = Client
        fields = ['Lname', 'Fname', 'Mname', 'email', 'phone', 'birthday', 'group', 'country' ]

    