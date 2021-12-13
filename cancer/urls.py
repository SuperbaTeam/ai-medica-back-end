from django.urls import path
from .views import CancerList, CancerDetail

urlpatterns = [
    path("", CancerList.as_view(), name="cancer_list"),
    path("<int:pk>/", CancerDetail.as_view(), name="cancer_detail"),
]
