from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

from first_app.models import Book, Genre, Author
from first_app.forms import GenreForm, BookForm
from first_app.filters import BookFilter




def main(request):
    search = request.GET.get('search')

    if search:
        book_list = Book.objects.filter(name__icontains=search, is_published=True)
    else:
        book_list = Book.objects.filter(is_published=True)
    
    genre_list = Genre.objects.all()

    filter_set = BookFilter(request.GET, queryset=book_list)

    offset = request.GET.get('offset', 1)
    limit = request.GET.get('limit', 2)

    paginator = Paginator(filter_set.qs, limit)
    book_list = paginator.get_page(offset)

    return render(request, 'index.html', {
        'book_list': book_list,
        'genre_list': genre_list,
        'filter': filter_set,
    })


def get_by_genres(request, id):
    genre_list = Genre.objects.all()
    book_list = Book.objects.filter(genres__id=id)
    return render(request, 'index.html', {
        'book_list': book_list,
        'genre_list': genre_list,   
    })


def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_detail.html', { 'book': book })


