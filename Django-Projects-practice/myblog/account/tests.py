from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# class UserModelTest(TestCase):
#     def test_create_user_and_check_name(self):
#         user = User.objects.create_user(
#             username='irfan',
#             password='test123',
#             first_name='Irfan',
#             last_name='Mulani'
#         )
#         self.assertEqual(user.first_name, 'Irfan')
#         self.assertEqual(user.last_name, 'Mulani')

# class AccountViewTest(TestCase):
#     def test_account_view_returns_correct_text(self):
#         response = self.client.get(reverse('account'))  
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Account Page")

