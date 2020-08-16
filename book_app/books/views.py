from django.shortcuts import render
from books.models import book

# Create your views here.
def book_index(request):
    books = book.objects.all().order_by('-read_on')
    context = {'books': books}
    return render(request, 'book_index.html', context)

def book_detail(request, pk):
    bookDetail = book.objects.get(pk=pk)
    context = {'bookDetail': bookDetail}
    return render(request, 'book_detail.html', context)