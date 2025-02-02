from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length = 150, unique = False, verbose_name="Категория")
    slug = models.SlugField(max_length = 150, unique = False, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("id",)

    def __str__(self):
        return self.name 


class Products(models.Model):
    name = models.CharField(max_length = 150, unique=False, blank = False, verbose_name = "Название")
    slug = models.SlugField(max_length = 150, unique=False, blank = False, verbose_name = "URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="goods_images", null = True, blank=True,verbose_name="изображение")
    price = models.DecimalField(default = 0.00, max_digits=7, decimal_places=2, verbose_name = "цена")
    quantity = models.PositiveIntegerField(default = 0, verbose_name = "количество")
    category = models.ForeignKey(to=Categories, on_delete = models.CASCADE, verbose_name = "Категория")

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
    
    def id_display(self):
        return f"{self.id:05}"