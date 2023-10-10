from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import UserProfile


class GetUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]
        extra_kwargs = {"is_staff": {"read_only": True}}


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        user_profile = UserProfile.objects.filter(user=user).first()
        token = super().get_token(user)
        token["is_staff"] = user.is_staff
        token["role"] = user_profile.role
        return token


class UserProfileSerializer(serializers.ModelSerializer):
    user = GetUserSerializer()

    class Meta:
        model = UserProfile
        fields = ["role", "user"]
