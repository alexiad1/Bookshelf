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
            data = requests.get(url=googleAPIURL,params=PARAMS).json()
            bookInfo = data['items'][0]['volumeInfo']

            newBook = book(
                title = bookInfo['title'],
                author = bookInfo['authors'][0],
                genre = bookInfo['categories'][0],
                page_count = bookInfo['pageCount'],
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
