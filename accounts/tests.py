from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model

from django.urls import reverse

from django.contrib.auth.models import User

from .models import CustomUser

from .models import Cancer

from rest_framework import status

from rest_framework.test import APITestCase

        


class CancerTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser2 = get_user_model().objects.create_user(
            username="test", password="test"
        )

        testuser2.save()

        testcancer = Cancer.objects.create(
            owner=testuser2,
           
            texture_mean=1,
           
            area_mean=1,
           
            smoothness_mean=1,
           
            compactness_mean=1,
           
            concavity_mean=1,
           
            concave_points_mean=1,
           
            state=1,
        )
        testcancer.save()