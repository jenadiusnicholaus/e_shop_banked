from django.urls import path, include
from rest_framework import routers
from .views import CategoryView


router = routers.DefaultRouter()
router.register(r"category", CategoryView)


urlpatterns = [
    path("v1/", include(router.urls)),
]
