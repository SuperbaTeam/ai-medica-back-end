from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CusotmUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")
