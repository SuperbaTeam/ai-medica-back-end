from django.urls import path

from .views import (
                    StrokeList,
                    StrokeDetail,
                    Stroke_Create
                    )

urlpatterns = [
    path('',StrokeList.as_view(),name="stroke_list"),
    path ('<int:pk>/',StrokeDetail.as_view(),name="stroke_detail"),
    path('create/',Stroke_Create,name="stroke_create"),    
]
