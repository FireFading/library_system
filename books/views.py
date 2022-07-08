from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Book


class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'
    
    def get_queryset(self):
        title = self.request.GET.get('title')
        author = self.request.GET.get('author')
        if title != "" and author != "":
            object_list = Book.objects.filter(
                Q(title__icontains=title) | Q(author__icontains=author)
            )
        else:
            if title == "":
                object_list = Book.objects.filter(
                Q(author__icontains=author)
            )
            else:
                object_list = Book.objects.filter(
                Q(title__icontains=title)
            )
        return object_list
    
    
def home(request):
    return render(request, "home.html")
