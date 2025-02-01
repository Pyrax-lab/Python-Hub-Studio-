from django.shortcuts import render
from .forms import UserLoginForm
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
        form = UserLoginForm


    return render(request, "users/login.html", context={"form": form})

def registration(request):
    return render(request, "users/registration.html")

def profile(request):
    return render(request, "users/profile.html")

def logout(request):
    ...#return render(request, "users/")