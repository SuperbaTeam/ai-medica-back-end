from django.conf import settings
from django.contrib import admin

from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
# from accounts.custom_claim import my_token_optain_per_view
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [

    path("api/admin/", admin.site.urls),
    path("api/cancer/", include("cancer.urls")),
    path("api/stroke/", include("stroke.urls")),
    path("api/hepatitis/", include("hepatitis.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/",
        # my_token_optain_per_view.as_view(),
        jwt_views.TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
