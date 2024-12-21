from django import forms 

from first_app.models import Genre, Book, Author



class GenreForm(forms.Form):
    name = forms.CharField(max_length=300, label='Название')



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'name',
            'year',
            'description',
            'rating',
            'language',
            'image',
            'author',
            'genres',
            'is_published',
        )


        widgets = {
            'name': forms.TextInput(attrs={'class': 'span_red', 'id': "name_id"},),
            'year': forms.NumberInput(),
            'description': forms.TextInput(),
            'rating': forms.NumberInput(),
            'language': forms.TextInput(),
            'image': forms.FileInput(),
            'author': forms.Select(),
            'genres': forms.CheckboxSelectMultiple(),

        }

