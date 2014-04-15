from django import template

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
              Template Filter Functions 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css})
