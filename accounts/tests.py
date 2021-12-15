from django.test import TestCase
from django.contrib.auth import get_user_model

class AccountTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser = get_user_model().objects.create_user(
            username="test",email="test@test.com", password="test"
        )

        testuser.save()
        cls.assertEqual(testuser.username, "test")
        
        cls.assertEqual(testuser.password, "test")