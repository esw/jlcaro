from django import template

register = template.Library()


@register.inclusion_tag('base/form.html')
def build_form(form):
    return { 'form': form }
