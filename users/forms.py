from django import forms 
from .models import User 
from django.contrib.auth.forms import AuthenticationForm # Используется только для Логина тоесть не создаёт нового пользователя
from django.contrib.auth.forms import UserCreationForm   # Используется только для Регистрации и создаёт нового пользователя


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(label= "Имя пользователя", widget=forms.TextInput(attrs={"autofocus": True,
                                                                                        "class":"form-control",
                                                                                        "placeholder": "Ваше имя"}))
    password = forms.CharField(label = "Пароль", widget=forms.PasswordInput(attrs={"authocomplete":"current-password",
                                                                                   "class":"form-control",
                                                                                   "placeholder":"Ваш пароль"}))
    class Meta:
        model = User
        fields = ["username", "password"]
        
    
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    username = forms.CharField()
    password1 = forms.CharField()
    password2 =forms.CharField()