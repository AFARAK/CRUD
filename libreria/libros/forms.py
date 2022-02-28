from django import forms
from .models import Author, Book

#Crear formulario autores
class AuthorForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Author

        #especificar los campos
        fields = [
            'first_name',
            'last_name',
            'photo',
            'birth_date'
        ]

#Formulario libros
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'year',
            'description',
            'author',
            'cost'
        ]