from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model

from django.urls import reverse

from django.contrib.auth.models import User

from .models import CustomUser

from .models import Cancer

from rest_framework import status

from rest_framework.test import APITestCase

        

