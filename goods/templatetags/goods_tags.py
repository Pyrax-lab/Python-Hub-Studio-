from goods.models import Categories 
from django.utils.http import urlencode
from django import template 

register = template.Library()

@register.simple_tag()
def goods_category():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)  # позволяет использовать переменную context тут
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)