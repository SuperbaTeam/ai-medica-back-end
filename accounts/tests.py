from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model
from django.urls import reverse

from django.contrib.auth.models import User

from .models import CustomUser


def setUpTestData(cls):
        
        testuser1 = User.objects.create_user(username="test", password="test")

        testuser1.save()

        

