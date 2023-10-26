from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "status"]
