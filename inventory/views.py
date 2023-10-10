from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category

from .serializers import CategorySerializers


# Category views set
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def get_object(self):
        # Use the desired lookup field from the URL
        lookup_value = self.kwargs.get(self.lookup_field)
        return get_object_or_404(
            Category, id=self.request.query_params.get("category_id", None)
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        _catogory_id = request.query_params.get("category_id", None)

        # get all catories  if no is specified
        if _catogory_id is None:
            serializer = self.get_serializer(queryset, many=True)
            if queryset.exists():
                response_obj = {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Found",
                    "data": {"categories": serializer.data},
                }
            return Response(data=response_obj, status=status.HTTP_200_OK)

        # if the id is specified then get  specific  category
        try:
            q = Category.objects.get(id=_catogory_id)
            serializer = self.get_serializer(q)

            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Found",
                "data": {"booking_state": serializer.data},
            }
            return Response(data=response_obj, status=status.HTTP_200_OK)
        except:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Not Found",
            }
            return Response(data=response_obj, status=status.HTTP_404_NOT_FOUND)

    # create a new category
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"message": "created"}, status=status.HTTP_201_CREATED)
        else:
            serializer.is_valid(raise_exception=True)
            return Response(
                {"message": "Failed to create a catgory"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, *args, **kwargs):
        _catogory_id = request.query_params.get("category_id", None)

        _status = request.data.get("status")
        _name = request.data.get("name")
        _description = request.data.get("description")

        instance = self.get_queryset().get(
            id=_catogory_id,
        )
        data = {
            "status": _status,
            "name": _name,
            "description": _description,
        }
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "message": "Record updated successfully",
            }
            return Response(response_obj, status=status.HTTP_201_CREATED)
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Failed to update",
            }
            Response(response_obj)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Deleted"})
