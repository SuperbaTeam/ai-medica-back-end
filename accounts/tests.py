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

class APITest(APITestCase):

    def testlist(self):
        
        response = self.client.get(reverse("cancer_list"))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testdetail(self):

        user_ = get_user_model().objects.create_user(
           
            username="test", password="test"
        )
        user_.save()

        testcancer = Cancer.objects.create(

            smoothness_mean=1,
        
            compactness_mean=1,
        
            concavity_mean=1,
        
            concave_points_mean=1,
        
            state=1,
           
            owner=user_,
        
            texture_mean=1,
        
            area_mean=1,
        
            smoothness_mean=1,
        
            compactness_mean=1,
        
            concavity_mean=1,
        
            concave_points_mean=1,
        
            state=1,
        )
        testcancer.save()

        response = self.client.get(reverse("cancerdetail", args=[1]))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(
         
            response.data,
            {
                "id": 1,
                
                "texture_mean": testcancer.texture_mean,
                
                "area_mean": testcancer.area_mean,
                
                "smoothness_mean": testcancer.smoothness_mean,
                
                "compactness_mean": testcancer.compactness_mean,
                
                "concavity_mean": testcancer.concavity_mean,
                
                "concave_points_mean": testcancer.concave_points_mean,
                
                "state": testcancer.state,
                
                "owner": user_.id,
            },
        )

    def testcreate(self):

        test_user = get_user_model().objects.create_user(
        
            username="test", password="test"
        )
        test_user.save()

        url = reverse("cancerlist")
        data = {
         
            "texture_mean": 999.0,
         
            "area_mean": 999.0,
         
            "smoothness_mean": 999.0,
         
            "compactness_mean": 999.0,
         
            "concavity_mean": 999.0,
         
            "concave_points_mean": 999.0,
         
            "state": 999.0,
         
            "owner": test_user.id,
        }
        self.client.login(username="test", password="test")
    
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(Cancer.objects.count(), 1)
    
        self.assertEqual(Cancer.objects.get().texture_mean, data["texture_mean"])

    def testupdate(self):
        test_user = get_user_model().objects.create_user(
          
            username="test", password="test"
        )
        test_user.save()

        test_cancer = Cancer.objects.create(
            owner=test_user,
          
            id=1,
          
            texture_mean=1,
          
            area_mean=1,
          
            smoothness_mean=1,
          
            compactness_mean=1,
          
            concavity_mean=1,
          
            concave_points_mean=1,
          
            state=1,
        )


        test_cancer.save()

        url = reverse("cancerdetail", args=[test_cancer.id])
      
        data = {
      
            "id": 1,
      
            "texture_mean": 999.0,
            "area_mean": 999.0,
      
            "smoothness_mean": 999.0,
      
            "compactness_mean": 999.0,
      
            "concavity_mean": 999.0,
      
            "concave_points_mean": 999.0,
      
            "state": 999.0,
      
            "owner": test_user.id,
      
        }
        self.client.login(username="test", password="test")

        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Cancer.objects.count(), test_cancer.id)
     
        self.assertEqual(Cancer.objects.get().id, data["id"])
