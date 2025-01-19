from django.shortcuts import render, get_list_or_404
from .models import Products
# Create your views here.


def catalog(request, catalog_slug):

    if catalog_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = catalog_slug))

    return render(request, "goods/catalog.html", {"goods": goods})

    


def product(request, product_slug):

    product = Products.objects.get(slug = product_slug)

    return render(request, "goods/product.html", {"product": product})