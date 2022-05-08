from django import template

register = template.library()

@register.filter(name='cut') # Register with decorators, otherwise down below register.filter('cut', cut)
def cut(value, arg):
    """
    This cuts of all values of "arg" from the string!
    """
    return value.replace(art,'')

# register.filter('cut', cut)
