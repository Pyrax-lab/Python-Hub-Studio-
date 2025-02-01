from django import forms 
from .models import User 
from django.contrib.auth.forms import AuthenticationForm # Используется только для Логина тоесть не создаёт нового пользователя

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(label= "Имя пользователя", widget=forms.TextInput(attrs={"autofocus": True,
                                                                                        "class":"form-control",
                                                                                        "placeholder": "Ваше имя"}))
    password = forms.CharField(label = "Пароль", widget=forms.PasswordInput(attrs={"authocomplete":"current-password",
                                                                                   "class":"form-control",
                                                                                   "placeholder":"Ваш пароль"}))
    class Meta:
        model = User
        