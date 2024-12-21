from django.urls import path

from workspace.views import (
    workspace_main,
    edit_book,
    delete_book,
    create_genre,
    create_book
)

urlpatterns = [
    path('', workspace_main, name='workspace_main'),
    path('edit-book/<int:id>', edit_book, name='edit_book'),
    path('book-delete/<int:id>/', delete_book, name='delete_book'),
    path('create-genre/', create_genre, name='create_genre'),
    path('create-book', create_book, name='create_book'),
]
