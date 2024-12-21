import django_filters
from django import forms

from first_app.models import *



class BookFilter(django_filters.FilterSet):
    genres = django_filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all(),
                                                      widget=forms.CheckboxSelectMultiple)
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all(), empty_label='choose',
                                              widget=forms.Select)
    
    class Meta:
        model = Book
        fields = (
            'genres',
            'author',
            'is_published',
        )
