from django.urls import path, include
from rest_framework import routers
from .views import ProductsViewSet


router = routers.DefaultRouter()
router.register(r"product_vset", ProductsViewSet)


urlpatterns = [
    path("v1/", include(router.urls)),
]
