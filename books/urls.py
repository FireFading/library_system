from django.urls import path, include

from .views import home, SearchResultsView


urlpatterns = [
    path('search/', SearchResultsView.as_view(), name="search"),
    path('', home, name="home"),
]
