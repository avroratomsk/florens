from django import template

register = template.Library()

@register.simple_tag()
def get_static(file):
    return '/core/theme/mb/' + file