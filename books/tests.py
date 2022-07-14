from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from .models import Book
from core.models import User
from .views import catalog, add_book, home, edit_book, new_book, delete_book, book, SearchResultsView


class BookTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
        )
        self.book = Book.objects.create(
            title='testbook',
            author='testuser',
            year=2015,
            number=3
        )
        self.client.force_login(user=self.user)
        
    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(),'/book/testbook')
        
    def test_book_str(self):
        book = Book.objects.get(id=1)
        self.assertEquals(str(book), "testbook by testuser, 2015")
        
    def test_delete_book(self):
        self.assertEquals(Book.objects.count(), 1)
        self.client.post(reverse("delete", args=["testbook"]))
        self.assertEquals(Book.objects.count(), 0)
        
    def test_add_book(self):
        self.assertEquals(Book.objects.count(), 1)
        self.client.post(reverse("new_book"), {"adding_title": "testing", "adding_author": "testauthor", "year": "2015", "number": "2"})
        self.assertEquals(Book.objects.count(), 2)
        
        
class BookAcessTest(TestCase):
    def test_anonymous_cannot_see_page(self):
        response = self.client.get(reverse("catalog"))
        self.assertRedirects(response, "/auth/signin/?next=/books-catalog/")
        response = self.client.get(reverse("home"))
        self.assertRedirects(response, "/auth/signin/?next=/")
        
    def test_authenticated_user_can_see_page(self):
        user = User.objects.create_user(username="username", email="example@gmail.com", password="some_pass")
        self.client.force_login(user=user)
        response = self.client.get(reverse("catalog"))
        self.assertEqual(response.status_code, 200)
        

class TestUrl(SimpleTestCase):
    
    def test_list_url_is_resolved_home(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)
        
    def test_list_url_is_resolved_catalog(self):
        url = reverse("catalog")
        self.assertEqual(resolve(url).func, catalog)
        
    def test_list_url_is_resolved_addbook(self):
        url = reverse("add")
        self.assertEqual(resolve(url).func, add_book)
        
    def test_list_url_is_resolved_newbook(self):
        url = reverse("new_book")
        self.assertEqual(resolve(url).func, new_book)
        
    def test_list_url_is_resolved_search(self):
        url = reverse("search")
        self.assertEqual(resolve(url).func.view_class, SearchResultsView)
        
        
class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
        )
        self.book = Book.objects.create(
            title='testbook',
            author='testuser',
            year=2015,
            number=3
        )
        self.client.force_login(user=self.user)
        
    def test_home(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        
    def test_catalog(self):
        response = self.client.get(reverse("catalog"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog.html")
        
    def test_addbook(self):
        response = self.client.get(reverse("add"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_book.html")
        
    def test_detail_book_page(self):
        response = self.client.get(reverse("book", args=["testbook"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book.html")
        
        