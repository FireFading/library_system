from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import wikipedia
import re

from .models import Book
from .forms import BooksFilterForm


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
    
    
@login_required(login_url='signin')
def catalog(request):
    books = Book.objects.all()
    if request.method == 'GET':
        form = BooksFilterForm(request.GET)
        if form.is_valid() and form.cleaned_data["ordering"]:
            books = books.order_by(form.cleaned_data["ordering"])
    else:
        form = BooksFilterForm()
    context = {
        "books": books,
        "form": form,
    }
    return render(request, "catalog.html", context)


@login_required(login_url='signin')
def home(request):
    return render(request, "home.html")


@login_required(login_url='signin')
def add_book(request):
    return render(request, "add_book.html")


def get_description(inf):
    wikipedia.set_lang("en")
    try:
        page = wikipedia.page(inf)
        wikitext = page.content[:1000]
        wikimas = wikitext.split(".")
        wikimas = wikimas[:-1]
        desc = ""
        for x in wikimas:
            if "==" in x:
                break
            if len(x.strip()) > 3:
                desc += f"{x}."
        desc = re.sub('\([^()]*\)', '', desc)
        desc = re.sub('\{[^\{\}]*\}', '', desc)
        return desc
    except Exception as e:
        return "This information is unknown. You can add description!"


@login_required(login_url='signin')
def new_book(request):
    if request.method == "POST":
        title = request.POST.get("adding_title")
        author = request.POST.get("adding_author")
        number = request.POST.get("number")
        year = request.POST.get("year")
        description = get_description(str(title))
        about_author = get_description(str(author))
        
        if title != "" and author != "" and number != "" and year != "":
            book = Book.objects.create(title=title, author=author, number=number, year=year, description=description, about_author=about_author)
            book.save()
            
            return redirect("catalog")
        
        return redirect("add")
    

@login_required(login_url='signin')
def delete_book(request, pk):
    if request.method == "POST":
        book = Book.objects.get(title=pk)
        book.delete()
    return redirect("catalog")


def book(request, pk):
    current_book = Book.objects.get(title=pk)
    is_editable = 0
    context = {
        'book': current_book,
        'is_editable': is_editable,
        }
    return render(request, 'book.html', context)


def edit_book(request, pk):
    current_book = Book.objects.get(title=pk)
    is_editable = 1
    context = {
        'book': current_book,
        'is_editable': is_editable,
        }
    return render(request, 'book.html', context)
