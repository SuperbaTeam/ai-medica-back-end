import json
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Hepatitis


class HepatitisModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_hepatitis = Hepatitis.objects.create(
            owner=test_user,
            name="Musab",
            email="Musab@test.com",
            mobile="0790187612",
            age=21,
            gender="1",
            steroid="1",
            antivirals="1",
            fatigue="1",
            malaise="1",
            anorexia="1",
            liver_big="1",
            liver_firm="1",
            spleen_palpable="2",
            spiders="1",
            ascites="1",
            varices="1",
            bilirubin=22.5,
            alk_phosphate=22.4,
            sgot=23.4,
            albumin=33.5,
            protime=22.0,
            histology="1",
        )

        test_hepatitis.save()

    def test_hepatitis_content(self):
        hepatitis = Hepatitis.objects.get(id=1)

        self.assertEqual(str(hepatitis.owner), "tester")

        self.assertEqual(hepatitis.name, "Musab")
        self.assertEqual(hepatitis.email, "Musab@test.com")
        self.assertEqual(hepatitis.mobile, "0790187612")
        self.assertEqual(hepatitis.age, 21)
        self.assertEqual(hepatitis.gender, "1")
        self.assertEqual(hepatitis.steroid, "1")
        self.assertEqual(hepatitis.antivirals, "1")
        self.assertEqual(hepatitis.fatigue, "1")
        self.assertEqual(hepatitis.malaise, "1")
        self.assertEqual(hepatitis.anorexia, "1")
        self.assertEqual(hepatitis.liver_big, "1")
        self.assertEqual(hepatitis.liver_firm, "1")
        self.assertEqual(hepatitis.spleen_palpable, "2")
        self.assertEqual(hepatitis.spiders, "1")
        self.assertEqual(hepatitis.ascites, "1")
        self.assertEqual(hepatitis.varices, "1")
        self.assertEqual(hepatitis.bilirubin, 22.5)
        self.assertEqual(hepatitis.alk_phosphate, 22.4)
        self.assertEqual(hepatitis.sgot, 23.4)
        self.assertEqual(hepatitis.albumin, 33.5)
        self.assertEqual(hepatitis.protime, 22.0)
        self.assertEqual(hepatitis.histology, "1")


class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse("hepatitis_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_hepatitis = Hepatitis.objects.create(
            owner=test_user,
            id=1,
            name="Musab",
            email="Musab@test.com",
            mobile="0790187612",
            age=21,
            gender="1",
            steroid="1",
            antivirals="1",
            fatigue="1",
            malaise="1",
            anorexia="1",
            liver_big="1",
            liver_firm="1",
            spleen_palpable="2",
            spiders="1",
            ascites="1",
            varices="1",
            bilirubin=22.5,
            alk_phosphate=22.4,
            sgot=23.4,
            albumin=33.5,
            protime=22.0,
            histology="1",
            status="live",
        )

        test_hepatitis.save()

        response = self.client.get(reverse("hepatitis_detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": 1,
                "name": test_hepatitis.name,
                "email": test_hepatitis.email,
                "mobile": test_hepatitis.mobile,
                "age": test_hepatitis.age,
                "gender": test_hepatitis.gender,
                "steroid": test_hepatitis.steroid,
                "antivirals": test_hepatitis.antivirals,
                "fatigue": test_hepatitis.fatigue,
                "malaise": test_hepatitis.malaise,
                "anorexia": test_hepatitis.anorexia,
                "liver_big": test_hepatitis.liver_big,
                "liver_firm": test_hepatitis.liver_firm,
                "spleen_palpable": test_hepatitis.spleen_palpable,
                "spiders": test_hepatitis.spiders,
                "ascites": test_hepatitis.ascites,
                "varices": test_hepatitis.varices,
                "bilirubin": test_hepatitis.bilirubin,
                "alk_phosphate": test_hepatitis.alk_phosphate,
                "sgot": test_hepatitis.sgot,
                "albumin": test_hepatitis.albumin,
                "protime": test_hepatitis.protime,
                "histology": test_hepatitis.histology,
                "status": test_hepatitis.status,
                "owner": test_user.id,
            },
        )

    def test_create(self):
        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        url = reverse("hepatitis_create")
        data = {
            # "id": 1,
            "name": "Jehad Abu Awwad",
            "email": "Jehadabuawwad@outlook.com",
            "mobile": "0790187612",
            "age": 24,
            "gender": "1",
            "steroid": "1",
            "antivirals": "1",
            "fatigue": "1",
            "malaise": "1",
            "anorexia": "1",
            "liver_big": "1",
            "liver_firm": "1",
            "spleen_palpable": 2,
            "spiders": "1",
            "ascites": "1",
            "varices": "1",
            "bilirubin": 22.5,
            "alk_phosphate": 22.4,
            "sgot": 23.4,
            "albumin": 33.5,
            "protime": 22.0,
            "histology": "1",
            "status": "live",
            "owner": test_user.id,
        }
        self.client.login(username="tester", password="pass")
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(Hepatitis.objects.count(), 1)
        self.assertEqual(Hepatitis.objects.get().name, data["name"])

    def test_delete(self):
        """Test the api can delete a hepatitis."""

        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_hepatitis = Hepatitis.objects.create(
            id=5,
            owner=test_user,
            name="Jehad Abu Awwad",
            email="Jehadabuawwad@outlook.com",
            mobile="0790187612",
            age=24,
            gender="1",
            steroid="1",
            antivirals="1",
            fatigue="1",
            malaise="1",
            anorexia="1",
            liver_big="1",
            liver_firm="1",
            spleen_palpable="2",
            spiders="1",
            ascites="1",
            varices="1",
            bilirubin=22.5,
            alk_phosphate=22.4,
            sgot=23.4,
            albumin=33.5,
            protime=22.0,
            histology="1",
            status="live",
        )

        test_hepatitis.save()

        hepatitis = Hepatitis.objects.get()

        url = reverse("hepatitis_detail", kwargs={"pk": hepatitis.id})
        self.client.login(username="tester", password="pass")

        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)

    # def test_update(self):
    #     test_user = get_user_model().objects.create_user(
    #         username="tester", password="pass"
    #     )
    #     test_user.save()

    #     test_hepatitis = Hepatitis.objects.create(
    #         owner=test_user,
    #         id=1,
    #         name="Jehad Abu Awwad",
    #         email="Jehadabuawwad@outlook.com",
    #         mobile="0790187612",
    #         age=24,
    #         gender="1",
    #         steroid="1",
    #         antivirals="1",
    #         fatigue="1",
    #         malaise="1",
    #         anorexia="1",
    #         liver_big="1",
    #         liver_firm="1",
    #         spleen_palpable="2",
    #         spiders="1",
    #         ascites="1",
    #         varices="1",
    #         bilirubin=22.5,
    #         alk_phosphate=22.4,
    #         sgot=23.4,
    #         albumin=33.5,
    #         protime=22.0,
    #         histology="1",
    #         status="live",
    #     )

    #     test_hepatitis.save()

    #     url = reverse("hepatitis_detail", args=[test_hepatitis.id])

    #     data = {
    #         "id": 1,
    #         "name": "Jehad Abu Awwad",
    #         "email": "Jehadabuawwad@outlook.com",
    #         "mobile": "0790187612",
    #         "age": 29,
    #         "gender": "1",
    #         "steroid": "1",
    #         "antivirals": "1",
    #         "fatigue": "1",
    #         "malaise": "1",
    #         "anorexia": "1",
    #         "liver_big": "1",
    #         "liver_firm": "1",
    #         "spleen_palpable": 2,
    #         "spiders": "1",
    #         "ascites": "1",
    #         "varices": "1",
    #         "bilirubin": 22.5,
    #         "alk_phosphate": 99.9,
    #         "sgot": 23.4,
    #         "albumin": 33.5,
    #         "protime": 22.0,
    #         "histology": "1",
    #         "status": "live",
    #         "owner": test_user.id,
    #     }
    #     self.client.login(username="tester", password="pass")

    #     response = self.client.put(url, data, format="json")

    #     self.assertEqual(response.status_code, status.HTTP_200_OK, url)

    #     self.assertEqual(Hepatitis.objects.count(), test_hepatitis.id)
    #     self.assertEqual(Hepatitis.objects.get().id, data["id"])
