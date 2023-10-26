from rest_framework import generics, status
from rest_framework.response import Response


class PaginateQuery:
    @staticmethod
    def paginate(self, page):
        serializer = self.get_serializer(page, many=True)
        paginated_response = self.get_paginated_response(serializer.data)
        page_size = self.pagination_class.page_size
        paginated_response.data["page_size"] = page_size
        return paginated_response


class ProductsListOrSingleObject:
    @staticmethod
    def get_single_or_alist(self, id, queryset):
        if id is None:
            page = self.paginate_queryset(queryset)
            paginated_response = PaginateQuery.paginate(self=self, page=page)
            return paginated_response

        else:
            q = self.get_object()
            serializer = self.get_serializer(q)
            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Found",
                "data": serializer.data,
            }
            return Response(data=response_obj, status=status.HTTP_200_OK)
