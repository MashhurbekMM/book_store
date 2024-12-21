from django.contrib import admin
from first_app.models import Book, Author, Genre, Comment

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms



class BookAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')

    class Meta:
        model = Book
        fields = '__all__'


class CommentStackedinline(admin.StackedInline):
    extra = 1
    model = Comment


# admin.site.register(Book)
# admin.site.register(Author)

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'rating')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'year')
    list_filter = ('year', 'genres')
    filter_horizontal = ('genres',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_display_links = ('id', 'full_name')
    search_fields = ('id', 'full_name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'book__name', 'date')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'book__name', 'name')


