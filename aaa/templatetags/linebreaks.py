from django import template
from django.utils.html import format_html


register = template.Library()

@register.filter(name='nl2br')
def nl2br(value):
	return format_html('<br>'.join(value.splitlines()))