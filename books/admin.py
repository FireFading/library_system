from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "year", "number")


admin.site.register(Book, BookAdmin)
