from django.urls import path

from first_app import views

urlpatterns = [
    path('', views.main, name='main'),
    path('book-detail/<int:id>/', views.book_detail, name='book_detail'),
    path('get-by-genres/<int:id>/', views.get_by_genres, name="get_by_genres"),
    
]
