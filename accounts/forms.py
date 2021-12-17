from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.db.models import fields
from .models import CustomUser


class CusotmUserCreationForm(UserCreationForm):
    class Meta:
        models = CustomUser
        fields = ("username", "email", "password")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = CustomUser
        fields = ("username", "email", "password")
