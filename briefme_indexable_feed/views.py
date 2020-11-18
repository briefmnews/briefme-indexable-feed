from itertools import chain

from rest_framework.generics import ListAPIView

from .serializers import BaseIndexableFeedSerializer


class BaseIndexableFeed(ListAPIView):
    queryset_list = []
    serializer_classes = {}
    serializer_class = BaseIndexableFeedSerializer

    def get_queryset(self):
        return list(chain(*self.queryset_list))

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["serializer_classes"] = self.serializer_classes
        return context
