from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Cancer


class CancerModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_cancer = Cancer.objects.create(
            owner=test_user,
            name="Ashley",
            email="ashley@test.com",
            age=23,
            texture_mean=1,
            area_mean=1,
            smoothness_mean=1,
            compactness_mean=1,
            concavity_mean=1,
            concave_points_mean=1,
            state=1,
        )
        test_cancer.save()

    def test_cancer_content(self):
        cancer = Cancer.objects.get(id=1)

        self.assertEqual(str(cancer.owner), "tester")
        self.assertEqual(cancer.name, "Ashley")
        self.assertEqual(cancer.email, "ashley@test.com")
        self.assertEqual(cancer.age, 23)
        self.assertEqual(cancer.texture_mean, 1)
        self.assertEqual(cancer.area_mean, 1)
        self.assertEqual(cancer.smoothness_mean, 1)
        self.assertEqual(cancer.compactness_mean, 1)
        self.assertEqual(cancer.concavity_mean, 1)
        self.assertEqual(cancer.concave_points_mean, 1)
        self.assertEqual(cancer.state, 1)
        self.assertEqual(cancer.id, 1)


class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse("cancer_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_cancer = Cancer.objects.create(
            owner=test_user,
            id=1,
            name="Ashley",
            email="ashley@test.com",
            age=23,
            texture_mean=1,
            area_mean=1,
            smoothness_mean=1,
            compactness_mean=1,
            concavity_mean=1,
            concave_points_mean=1,
            state=1,
        )
        test_cancer.save()

        response = self.client.get(reverse("cancer_detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": 1,
                "name": test_cancer.name,
                "email": test_cancer.email,
                "age": test_cancer.age,
                "texture_mean": test_cancer.texture_mean,
                "area_mean": test_cancer.area_mean,
                "smoothness_mean": test_cancer.smoothness_mean,
                "compactness_mean": test_cancer.compactness_mean,
                "concavity_mean": test_cancer.concavity_mean,
                "concave_points_mean": test_cancer.concave_points_mean,
                "state": test_cancer.state,
                "owner": test_user.id,
            },
        )

    def test_create(self):
        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        url = reverse("cancer_create")
        data = {
            "name": "Ashley",
            "email": "ashley@test.com",
            "age": 23,
            "texture_mean": 999.0,
            "area_mean": 999.0,
            "smoothness_mean": 999.0,
            "compactness_mean": 999.0,
            "concavity_mean": 999.0,
            "concave_points_mean": 999.0,
            "state": 999.0,
            "owner": test_user.id,
        }
        self.client.login(username="tester", password="pass")
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(Cancer.objects.count(), 1)
        self.assertEqual(Cancer.objects.get().name, data["name"])

    def test_update(self):
        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_cancer = Cancer.objects.create(
            owner=test_user,
            id=1,
            name="Ashley",
            email="ashley@test.com",
            age=23,
            texture_mean=1,
            area_mean=1,
            smoothness_mean=1,
            compactness_mean=1,
            concavity_mean=1,
            concave_points_mean=1,
            state=1,
        )

        test_cancer.save()

        url = reverse("cancer_detail", args=[test_cancer.id])
        data = {
            "id": 1,
            "name": "Ashley",
            "email": "ashley@test.com",
            "age": 23,
            "texture_mean": 999.0,
            "area_mean": 999.0,
            "smoothness_mean": 999.0,
            "compactness_mean": 999.0,
            "concavity_mean": 999.0,
            "concave_points_mean": 999.0,
            "state": 999.0,
            "owner": test_user.id,
        }
        self.client.login(username="tester", password="pass")

        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Cancer.objects.count(), test_cancer.id)
        self.assertEqual(Cancer.objects.get().id, data["id"])

    def test_delete(self):
        """Test the api can delete a Cancer."""

        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_cancer = Cancer.objects.create(
            owner=test_user,
            id=6,
            name="Ashley",
            email="ashley@test.com",
            age=23,
            texture_mean=44444.0,
            area_mean=4444.0,
            smoothness_mean=444.0,
            compactness_mean=4444.0,
            concavity_mean=444.0,
            concave_points_mean=444.0,
            state=444.0,
        )

        test_cancer.save()

        cancer = Cancer.objects.get()

        url = reverse("cancer_detail", kwargs={"pk": cancer.id})
        self.client.login(username="tester", password="pass")

        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)
