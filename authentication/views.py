from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import CreateUserSerializer, GetUserSerializer, UserProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from .models import UserProfile


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_profile, create = UserProfile.objects.get_or_create(user=user)
            user.user_profile.save()
            response_data = {
                "message": "User created successfully.",
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = (
        "id"  # Customize the lookup field as needed (e.g., 'username', 'email')
    )

    def get(self, request, *args, **kwargs):
        # Get the user object associated with the request user (authenticated user)
        user = self.request.user

        # You can customize this logic to retrieve the user profile as needed
        # For example, you might want to retrieve the profile associated with the authenticated user
        # or retrieve the profile based on some other criteria.

        # Here, we'll use the authenticated user's ID to retrieve the profile
        try:
            profile = UserProfile.objects.get(id=user.id)
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(
                {"detail": "User profile not found."}, status=status.HTTP_404_NOT_FOUND
            )
