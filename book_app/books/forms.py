from django import forms

class newBookForm(forms.Form):
    bookTitle = forms.CharField(
        max_length=255,
        label='',
        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter book title'})
        )

    author = forms.CharField(
        max_length=255,
        label='',
        widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':'Author'}),
        required=False
    )