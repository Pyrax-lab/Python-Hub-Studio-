from django.urls import path 
from . import views

app_name = "goods"


urlpatterns = [
    path("serch", views.catalog, name="search"),
    path("<slug:catalog_slug>", views.catalog, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product")
]