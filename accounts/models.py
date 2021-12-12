from django.contrib.auth import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    email=models.models.EmailField( unique=True,max_length=254,verbose_name="Email Address")

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=["username","name","mobile","password"]

    class Meta:

        verbose_name="Person"

        verbose_name_plural="People"    

    def __str__(self):

        return self.email