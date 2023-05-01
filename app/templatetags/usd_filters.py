from django import template

register=template.Library()

def swap(value):
    return value.swapcase()


def count(value,arg):
    c=0
    for i in value:
        if i==arg:
            c+=1
        
    return c
@register.filter()
def rev(value):
    x=value[::-1]
    return x


register.filter('swap',swap)
register.filter('count',count)