from django import template
from urllib.parse import unquote

register = template.Library()

@register.filter
def urldecode(value):
    return unquote(value)
@register.filter(name='is_list')
def is_list(value):
    return isinstance(value, list)