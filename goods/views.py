from django.shortcuts import render, get_list_or_404
from .models import Products
from django.core.paginator import Paginator
from django.utils.http import urlencode
# Create your views here.


def catalog(request, catalog_slug):


    order_by1 = request.GET.get("order_by", None)
    on_sale = request.GET.get("on_sale", None)
    current_slug = catalog_slug

    print(order_by1)
    print(on_sale)

    if catalog_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = catalog_slug))

    if order_by1 and order_by1 != "default":
        print("11")
        goods = goods.order_by(order_by1)
    if on_sale:
        
        goods = goods.filter(price__lt=200)

    # get_page = 1
    # if request.method == "GET":
    #     if request.GET.get('page'):
    #         get_page = request.GET.get('page', 1)

    get_page = request.GET.get('page', 1)

    get_request = urlencode(request.GET.dict())
    print(get_request)
    paginator = Paginator(goods, 3)
    curent_page = paginator.page(get_page)

    return render(request, "goods/catalog.html", {"goods": curent_page, "current_slug": current_slug, "get_request": get_request})

    


def product(request, product_slug):

    product = Products.objects.get(slug = product_slug)

    return render(request, "goods/product.html", {"product": product})