from types import ClassMethodDescriptorType
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser
from .forms import CusotmUserCreationForm,CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form=CusotmUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=[
       "username",
        "email",
        "password"
        
    ]
admin.site.register(CustomUser,CustomUserAdmin)