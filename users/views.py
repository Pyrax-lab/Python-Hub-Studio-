from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
#from django.contrib import lo
# Create your views here.


def login(request):
    
    messages.success(request, "Успешно вошли")
    # #ip = request.META.get("HTTP_X_FORWARDED_FOR")
    # ip = request.META.get("REMOTE_ADDR")
    # print(ip)

    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        print("yes1")
        if form.is_valid():
            print("yes")
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form


    return render(request, "users/login.html", context={"form": form})

def registration(request):

    messages.success(request, "Успешно зарегестрировались")

    form = UserRegisterForm() 

    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("users:login"))
    else:
        form

    return render(request, "users/registration.html", context={"form":form})

def profile(request):
    return render(request, "users/profile.html")

def logout(request):
    auth.logout(request)
    return redirect(reverse("users:login"))
    ...#return render(request, "users/")