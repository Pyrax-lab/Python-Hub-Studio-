from django.shortcuts import render
from goods.models import Categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
# Create your views here.


def index(request):
    categories = Categories.objects.all()
    return render(request, "main/index.html", {"categories": categories})





def blog(request):
    return render(request, "main/about.html")