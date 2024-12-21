from django.db import models
from django.db.models import Model


class Author(Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = 'Авторы'
    
    full_name = models.CharField(verbose_name='ФИО', max_length=200)
    image = models.ImageField(verbose_name='изображение', upload_to='authorImages',)

    def __str__(self) -> str:
        return self.full_name
    

class Genre(Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    name = models.CharField(verbose_name='название', max_length=300)

    def __str__(self) -> str:
        return self.name
    


class Book(models.Model):

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    name = models.CharField(verbose_name='название', max_length=200)
    year = models.IntegerField(verbose_name='год выпуска')
    description = models.CharField(verbose_name='описание', max_length=300)
    rating = models.IntegerField(verbose_name='рейтинг')
    language = models.CharField(verbose_name='язык', max_length=200)
    image = models.ImageField(verbose_name='изображение', upload_to='images/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор книги')

    genres = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='books')

    is_published = models.BooleanField(default=True, verbose_name='публичность')


    def __str__(self) -> str:
        return f'{self.name} - {self.year}'
    



class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-date',)

    name = models.CharField(verbose_name='Имя', max_length=200)
    text = models.CharField(verbose_name='текст', max_length=400)
    book = models.ForeignKey('first_app.Book', on_delete=models.CASCADE, related_name='comments', verbose_name='Книга')
    date = models.DateTimeField(verbose_name='дата', auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.book.name}'
    