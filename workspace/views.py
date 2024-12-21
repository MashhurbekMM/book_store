from django.shortcuts import render, get_object_or_404,redirect

from first_app.models import Book, Author, Genre
from first_app.forms import BookForm, GenreForm
from workspace.decorators import login_required_custom

@login_required_custom
def workspace_main(request):
    book_list = Book.objects.all()    

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/workspace/')
            
    form = BookForm()
    genre_list = Genre.objects.all()
    author_list = Author.objects.all()

    return render(request, 'workspace/index.html', {
        'form': form,
        'author_list': author_list,
        'genre_list': genre_list,
        'book_list': book_list,
    })





@login_required_custom
def create_book(request):
    book_list = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/workspace/')
    form = BookForm()

    return render(request, 'workspace/create_book.html', {
        'form': form,
        'book_list': book_list,
    })
    

@login_required_custom
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/workspace/')
            
    form = BookForm(instance=book)

    genre_list = Genre.objects.all()
    author_list = Author.objects.all()
    return render(request, 'workspace/edit_book.html', {
        'author_list': author_list,
        'genre_list': genre_list,
        'book': book,
        'form': form,
    })



@login_required_custom
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/workspace/')


@login_required_custom
def create_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre_name = form.cleaned_data.get('name')
            print(form.cleaned_data)
            Genre.objects.create(
                name=genre_name
            )
            return redirect('/workspace/')
        
    form = GenreForm()
    return render(request, 'workspace/create_genre.html', {
        'form': form,
    })