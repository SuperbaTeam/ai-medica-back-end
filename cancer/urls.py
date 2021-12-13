from django.urls import path
from .views import CancerList, CancerDetail

urlpatterns = [
    path("", CancerList.as_view(), name="Cancer_List"),
    path("<int:pk>/", CancerDetail.as_view(), name="Cancer_Detail"),
]