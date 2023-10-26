from django.shortcuts import render
from rest_framework import viewsets

from Helpers.helpers import ProductsListOrSingleObject
from .models import Product
from .serializers import ProductSerializers
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get_object(self):
        return get_object_or_404(
            Product, id=self.request.query_params.get("product_id", None)
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).order_by("-date_created")
        product_id = request.query_params.get("product_id", None)
        # get all object  if no object id is specified
        return ProductsListOrSingleObject.get_single_or_alist(
            self, id=product_id, queryset=queryset
        )

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
        instance = self.get_object()
        data = data = request.data
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
