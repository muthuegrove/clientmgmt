'''
Template Tags for ClientManagement
'''
from django import template
register = template.Library()


@register.filter
def multiply(value, arg):
    if value and arg:
        return value*arg
    else:
        return 0.0
