from django.urls import path, include

from .views import catalog, add_book, home, new_book, delete_book, SearchResultsView


urlpatterns = [
    path('search/', SearchResultsView.as_view(), name="search"),
    path('books-catalog/', catalog, name="catalog"),
    path('add-book/', add_book, name="add"),
    path('add-book-success/', new_book, name="new_book"),
    path('delete-book/<str:pk>', delete_book, name="delete"),
    path('', home, name="home"),
]

