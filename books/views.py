from django.shortcuts import render, redirect
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
            return Book.objects.filter(Q(title__icontains=title) | Q(author__icontains=author))

        else:
            return Book.objects.filter(Q(author__icontains=author)) if title == "" else Book.objects.filter(Q(title__icontains=title))
    
    
def catalog(request):
    books = Book.objects.all().order_by("author")
    context = {
        "books": books,
    }
    return render(request, "catalog.html", context)


def home(request):
    return render(request, "home.html")


def add_book(request):
    return render(request, "add_book.html")


def new_book(request):
    if request.method == "POST":
        title = request.POST.get("adding_title")
        author = request.POST.get("adding_author")
        number = request.POST.get("number")
        year = request.POST.get("year")
        
        if title != "" and author != "" and number != "" and year != "":
            book = Book.objects.create(title=title, author=author, number=number, year=year)
            book.save()
            
            return redirect("home")
        
        return redirect("add")