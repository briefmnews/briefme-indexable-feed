from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .authentication import QueryStringAuthentication
from .serializers import BaseIndexableFeedSerializer


class IndexableFeedPagination(PageNumberPagination):
    page_size = 30
    max_page_size = 100
    page_size_query_param = "page_size"


class ConcatenatedQuerySet:
    ordered = True

    def __init__(self, querysets):
        self.querysets = querysets

    def count(self):
        return sum(queryset.count() for queryset in self.querysets)

    def __getitem__(self, key):
        remaining_offset = key.start
        remaining_limit = key.stop - remaining_offset
        results = []
        for queryset in self.querysets:
            if remaining_limit <= 0:
                break
            queryset_count = queryset.count()
            if remaining_offset >= queryset_count:
                remaining_offset -= queryset_count
                continue
            chunk = queryset[remaining_offset : remaining_offset + remaining_limit]
            results.extend(chunk)
            remaining_limit -= len(chunk)
            remaining_offset = 0
        return results


class BaseIndexableFeed(ListAPIView):
    queryset_list = []
    serializer_classes = {}
    serializer_class = BaseIndexableFeedSerializer
    authentication_classes = (QueryStringAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = IndexableFeedPagination

    def get_queryset(self):
        querysets = []
        for queryset in self.queryset_list:
            queryset = queryset.all()
            if not queryset.ordered:
                queryset = queryset.order_by("pk")
            querysets.append(queryset)
        return ConcatenatedQuerySet(querysets)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["serializer_classes"] = self.serializer_classes
        return context
