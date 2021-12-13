from django.urls import path

from .views import (
                    HepatitisList,
                    HepatitisDetail,
                    Hepatitis_Create
                    )

urlpatterns = [
    path('',HepatitisList.as_view(),name="hepatitis_list"),
    path ('<int:pk>/',HepatitisDetail.as_view(),name="hepatitis_detail"),
    path('create/',Hepatitis_Create,name="hepatitis_create"),    
]
