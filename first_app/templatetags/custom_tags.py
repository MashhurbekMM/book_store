from django import template

from first_app.models import Genre

register = template.Library()



@register.simple_tag
def get_all_genres():
    return Genre.objects.all()