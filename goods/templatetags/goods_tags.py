from goods.models import Categories 

from django import template 

register = template.Library()

@register.simple_tag()
def goods_category():
    return Categories.objects.all()