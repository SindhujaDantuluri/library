from django import forms
from django.contrib.auth.models import User
from . import models

class BookForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = ('title', 'author', 'image', 'status','borrowed_at')


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Genre
        fields = ('title', 'created_at')

