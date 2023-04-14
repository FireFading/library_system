from books.models import Book
from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "year", "number")


admin.site.register(Book, BookAdmin)
