from django import template
from django.apps import apps


register = template.Library()

@register.filter
def app_name(value):
    return value._meta.model_name


@register.filter(name='model_name')
def model_name(obj):
    """Returns the model name of an object."""
    return obj._meta.model_name


@register.filter(name='is_app')
def is_app(obj, app_name):
    """
    Checks if the given object belongs to the specified app.
    """
    try:
        model = obj._meta.model if hasattr(obj, '_meta') else obj.__class__
        return apps.get_containing_app_config(model.__module__).name == app_name
    except:
        return False