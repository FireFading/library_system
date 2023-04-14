from books.views import SearchResultsView, add_book, book, catalog, delete_book, edit_book, home, new_book
from django.urls import path

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search"),
    path("books-catalog/", catalog, name="catalog"),
    path("add-book/", add_book, name="add"),
    path("add-book-success/", new_book, name="new_book"),
    path("delete-book/<str:pk>", delete_book, name="delete"),
    path("book/<str:pk>", book, name="book"),
    path("book/<str:pk>/edit", edit_book, name="edit"),
    path("", home, name="home"),
]
