from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response

from Helpers.helpers import ProductsListOrSingleObject
from .models import Category

from .serializers import CategorySerializers


# Category views set
class CategoryView(viewsets.ModelViewSet):
    """
    This  product query set, where by you can do the from action in this
    view set,
    1. You get a list if  catagory )
    2. You can get a single Category object
    3. You can post a new  product
    4. You can  Edit the specific product  details by
    5. you can delete a specific category
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def get_object(self):
        # Use the desired lookup field from the URL
        lookup_value = self.kwargs.get(self.lookup_field)
        return get_object_or_404(
            Category, id=self.request.query_params.get("category_id", None)
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).order_by("-date_created")

        _catogory_id = request.query_params.get("category_id", None)

        # get all catories  if no is specified
        return ProductsListOrSingleObject.get_single_or_alist(
            self, id=_catogory_id, queryset=queryset
        )

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

        serializer = self.get_serializer(
            self.get_object(), data=request.data, partial=True
        )
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
