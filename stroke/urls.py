from django.urls import path

from .views import (
                    StrokeList,
                    StrokeDetail,
                    Stroke_Create
                    )

urlpatterns = [
    path('create/',Stroke_Create,name="stroke_create"),
    path('list/',StrokeList.as_view(),name="stroke_list"),
    path ('detail/<int:pk>/',StrokeDetail.as_view(),name="stroke_detail"),
    
]
