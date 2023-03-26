from django.urls import include, path

from .views import (
    add_book,
    book,
    catalog,
    delete_book,
    edit_book,
    home,
    new_book,
    SearchResultsView,
)


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
