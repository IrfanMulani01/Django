from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTest(TestCase):
    def test_create_user_and_check_name(self):
        user = User.objects.create_user(
            username='irfan',
            password='test123',
            first_name='Irfan',
            last_name='Mulani'
        )
        self.assertEqual(user.first_name, 'Irfan')
        self.assertEqual(user.last_name, 'Mulani')
