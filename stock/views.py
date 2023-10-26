from django.shortcuts import render
from rest_framework import viewsets
from stock.models import Stock
from .serializers import StockSerializers
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from Helpers.helpers import PaginateQuery as paginator, ProductsListOrSingleObject


# Create your views here.


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializers

    def get_object(self):
        return get_object_or_404(
            Stock, id=self.request.query_params.get("stock_id", None)
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).order_by("-date_created")
        _catogory_id = request.query_params.get("stock_id", None)

        # get all stock  if no object id is specified
        return ProductsListOrSingleObject.get_single_or_alist(
            self, id=_catogory_id, queryset=queryset
        )
