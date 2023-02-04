from django import forms
from .models import Hepatitis


class InputUserInfo(forms.Form):
    class Meta:
        model = Hepatitis
        fields = [
            "name",
            "email",
            "mobile",
            "age",
            "sex",
            "steroid",
            "antivirals",
            "fatigue",
            "malaise",
            "anorexia",
            "liver_big",
            "liver_firm",
            "spleen_palpable",
            "spiders",
            "ascites",
            "varices",
            "bilirubin",
            "alk_phosphate",
            "sgot",
            "albumin",
            "protime",
            "histology",
        ]
