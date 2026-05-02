from django.test import TestCase

class SimpleText(TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 3)