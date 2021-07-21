from django import template

register = template.Library()

# function for custom template filter
# 2nd way to register filter using decorators
@register.filter(name='mycut')
def cut(value, arg):
    """
    this cuts out all values of arg from the string
    """
    return value.replace(arg, "")


# 2nd way is to use decorators to register the filter
# register the custom filter
# register.filter('mycut', cut)
