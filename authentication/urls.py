from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("v1/register/", CreateUserView.as_view(), name="create_user"),
    path("v1/user-profile/", GetUserProfileView.as_view(), name="get_user_profile"),
]
