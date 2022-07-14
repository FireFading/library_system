from django.test import TestCase

from .models import Book
from core.models import User


class BookTest(TestCase):
    
    def setUp(self):
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
        
    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(),'/book/testbook')
        
