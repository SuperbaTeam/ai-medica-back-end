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


    def test_content(self):
        data_cancer = Cancer.objects.get(id=1)

        self.assertEqual(str(data_cancer.owner), "test")
        

        self.assertEqual(data_cancer.compactness_mean, 1)
        
        self.assertEqual(data_cancer.concavity_mean, 1)
        
        self.assertEqual(data_cancer.concave_points_mean, 1)
        
        self.assertEqual(data_cancer.state, 1)
        
        self.assertEqual(data_cancer.id, 1)


        self.assertEqual(data_cancer.texture_mean, 1)

        self.assertEqual(data_cancer.area_mean, 1)

        self.assertEqual(data_cancer.smoothness_mean, 1)
