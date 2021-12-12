from django.contrib.auth.models import AbstractUser

from django.db import models

class Account_Info(AbstractUser):  #Person


    email_account = models.EmailField(unique=True, max_length=100,verbose_name="Email Address Accunt")


    USERNAME_FIELD = 'email_account'

    REQUIRED_FIELDS = ['name', 'mobile','username','password']

    class Meta:

        verbose_name = "Account_Info"

        verbose_name_plural = "accounts"

    def __str__(self) -> str:

        return self.email_account