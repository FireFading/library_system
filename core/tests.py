from django.test import TestCase
from django.utils import timezone

from .models import User


class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        
    def test_created_at(self):
        user = User.objects.get(id=1)
        now = timezone.now()
        time = user.created_at
        self.assertEquals(time.strftime('%d-%m-%Y %H:%M'), now.strftime('%d-%m-%Y %H:%M'))

    def test_username_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')
        
    def test_is_staff(self):
        user = User.objects.get(id=1)
        is_staff = user.is_staff
        self.assertEquals(is_staff, False)
        
    def test_is_active(self):
        user = User.objects.get(id=1)
        is_active = user.is_active
        self.assertEquals(is_active, True)