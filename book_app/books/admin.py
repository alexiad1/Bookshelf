from django.contrib import admin
from books.models import book

# Register your models here.
class bookAdmin(admin.ModelAdmin):
    pass

admin.site.register(book, bookAdmin)