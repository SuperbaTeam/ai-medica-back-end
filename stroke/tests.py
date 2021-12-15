from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Stroke


class StrokeModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username="test", password="test"
        )
        test_user.save()

        test_stroke = Stroke.objects.create(
            name="Jehad Abu Awwad",
            email="Jehadabuawwad@outlook.com",
            mobile=790187612,
            age=24,
            bmi=18.0,
            avg_glucose_level=81.0,
            gender="True",
            residence_type="True",
            ever_married="False",
            work_type="1, 0, 0, 0, 0",
            smoking_status="1, 0, 0, 0",
            hypertension="True",
            heart_disease="False",
            status="Positve",
            owner=test_user,
        )

        test_stroke.save()

    def test_stroke_content(self):
        stroke = Stroke.objects.get(id=1)

        self.assertEqual(str(stroke.owner), "test")
        self.assertEqual(stroke.name, "Jehad Abu Awwad")
        self.assertEqual(stroke.email, "Jehadabuawwad@outlook.com")
        self.assertEqual(stroke.mobile, 790187612)
        self.assertEqual(stroke.age, 24)
        self.assertEqual(stroke.bmi, 18.0)
        self.assertEqual(stroke.avg_glucose_level, 81.0)
        self.assertEqual(stroke.gender, "True")
        self.assertEqual(stroke.residence_type, "True")
        self.assertEqual(stroke.ever_married, "False")
        self.assertEqual(stroke.work_type, "1, 0, 0, 0, 0")
        self.assertEqual(stroke.smoking_status, "1, 0, 0, 0")
        self.assertEqual(stroke.hypertension, "True")
        self.assertEqual(stroke.heart_disease, "False")
        self.assertEqual(stroke.status, "Positve")


class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse("stroke_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_stroke = Stroke.objects.create(
            name="Jehad Abu Awwad",
            email="Jehadabuawwad@outlook.com",
            mobile=790187612,
            age=24,
            bmi=18.0,
            avg_glucose_level=81.0,
            gender="True",
            residence_type="True",
            ever_married="False",
            work_type="1, 0, 0, 0, 0",
            smoking_status="1, 0, 0, 0",
            hypertension="True",
            heart_disease="False",
            status="Positve",
            owner=test_user,
        )

        test_stroke.save()

        response = self.client.get(reverse("stroke_detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": 1,
                "name": test_stroke.name,
                "email": test_stroke.email,
                "mobile": test_stroke.mobile,
                "age": test_stroke.age,
                "bmi": test_stroke.bmi,
                "avg_glucose_level": test_stroke.avg_glucose_level,
                "gender": test_stroke.gender,
                "residence_type": test_stroke.residence_type,
                "ever_married": test_stroke.ever_married,
                "work_type": test_stroke.work_type,
                "smoking_status": test_stroke.smoking_status,
                "hypertension": test_stroke.hypertension,
                "heart_disease": test_stroke.heart_disease,
                "status": test_stroke.status,
                "owner": test_user.id,
            },
        )

    def test_create(self):

        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()
        url = reverse("stroke_create")
        data = {
            "name": "Jehad Abu Awwad",
            "email": "Jehadabuawwad@outlook.com",
            "mobile": 790187612,
            "age": 24,
            "bmi": 18.0,
            "avg_glucose_level": 81.0,
            "gender": 1,
            "residence_type": 1,
            "ever_married": 0,
            "work_type": "1, 0, 0, 0, 0",
            "smoking_status": "1, 0, 0, 0",
            "hypertension": 1,
            "heart_disease": 0,
            "status": "Positve",
            "owner": test_user.id,
        }

        self.client.login(username="tester", password="pass")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)
        self.assertEqual(Stroke.objects.count(), 1)
        self.assertEqual(Stroke.objects.get().name, data["name"])

    def test_delete(self):
        """Test the api can delete a Stroke."""

        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_stroke = Stroke.objects.create(
            id=5,
            name="Jehad Abu Awwad",
            email="Jehadabuawwad@outlook.com",
            mobile=790187612,
            age=24,
            bmi=18.0,
            avg_glucose_level=81.0,
            gender="True",
            residence_type="True",
            ever_married="False",
            work_type="1, 0, 0, 0, 0",
            smoking_status="1, 0, 0, 0",
            hypertension="True",
            heart_disease="False",
            status="Positve",
            owner=test_user,
        )

        test_stroke.save()

        stroke = Stroke.objects.get()

        url = reverse("stroke_detail", kwargs={"pk": stroke.id})
        self.client.login(username="tester", password="pass")

        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)
