from django import forms

class newBookForm(forms.Form):
    bookTitle = forms.CharField(max_length=255,label='Add a New Book')