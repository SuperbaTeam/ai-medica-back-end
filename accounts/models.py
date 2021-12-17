from django.contrib.auth import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.models.EmailField(
        unique=True, max_length=254, verbose_name="Email Address"
    )

    REQUIRED_FIELDS = ["email", "password"]

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return self.username
