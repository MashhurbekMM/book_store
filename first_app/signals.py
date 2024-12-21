from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver

from .models import Book, Genre, Author


@receiver(pre_save, sender=Book)
def book_pre_create_signal(sender, instance, **kwargs):
    if instance.pk is None:
        print('Signal pre save for a new book')
    else: 
        print('Signal pre save for an existing book')



@receiver(post_save, sender=Book)
def book_create_signal(sender, instance, created, **kwargs):
    if created:
        print(f'The book{instance.name} was created')



@receiver(post_delete, sender=Book)
def book_create_signal(sender, instance, **kwargs):
    print(f'The movie {instance.name} was deleted')