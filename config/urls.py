from django.conf import settings
from django.contrib import admin

from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from accounts.views import MyObtainTokenPairView,RegisterView
urlpatterns = [

    path("api/admin/", admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path("api/cancer/", include("cancer.urls")),
    path("api/stroke/", include("stroke.urls")),
    path("api/hepatitis/", include("hepatitis.urls")),
    path(
        "api/token/",
        MyObtainTokenPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
