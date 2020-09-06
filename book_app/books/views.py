from django.shortcuts import render
from books.models import book
from books.forms import newBookForm
import json, requests, os

# Create your views here.
def book_index(request):
    if request.method == 'POST':
        form = newBookForm(request.POST)
        if form.is_valid():
            googleAPIURL = 'https://www.googleapis.com/books/v1/volumes'
            PARAMS = {'key': os.environ.get('googleBookKey') ,'q':form.cleaned_data['bookTitle'], 'maxResults': '1'}
            if form.cleaned_data['author'] != None:
                PARAMS['q'] += ' inauthor:' + form.cleaned_data['author']
            data = requests.get(url=googleAPIURL,params=PARAMS).json()
            bookInfo = data['items'][0]['volumeInfo']

            newBook = book(
                title = bookInfo['title'] if 'title' in bookInfo else'N/A',
                author = bookInfo['authors'][0] if 'authors' in bookInfo else 'N/A',
                genre= bookInfo['categories'][0] if 'categories' in bookInfo else 'N/A',
                page_count = bookInfo['pageCount'] if 'pageCount' in bookInfo else 0,
            )
            newBook.save()

    else:
        form = newBookForm()

    books = book.objects.all().order_by('read_on')
    context = {'books': books, 'form':form}
    return render(request, 'book_index.html', context)

def book_detail(request, pk):
    bookDetail = book.objects.get(pk=pk)
    context = {'bookDetail': bookDetail}
    return render(request, 'book_detail.html', context)
