from bleach import clean
from collections import OrderedDict
from django.utils.html import strip_tags
from rest_framework import serializers


class BaseIndexableFeedSerializer(serializers.Serializer):
    """Serializer that renders each instance with its own specific serializer"""

    def get_serializer(self, model):
        serializer_classes = self.context["serializer_classes"]
        return serializer_classes[model]

    def to_representation(self, instance):
        serializer = self.get_serializer(instance.__class__)
        return serializer(instance, context=self.context).data


def extract_indexable_content(data, fields):
    # Ordering the fields in te dictionary
    if all(field in data.keys() for field in fields):
        data = OrderedDict([(el, data[el]) for el in fields])

    searchable = ""
    for k, v in data.items():
        if isinstance(v, dict):
            bit = extract_indexable_content(v, fields)
            searchable += f" {bit}"
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, str):
                    if k in fields:
                        searchable += f" {i}"
                else:
                    bit = extract_indexable_content(i, fields)
                    searchable += f" {bit}"
        else:
            if k in fields:
                searchable += f" {v}"
    return searchable


def get_indexable_content(data, fields):
    indexable_content = extract_indexable_content(data, fields)
    return strip_tags(indexable_content).strip()


def get_summary_content(data, fields):
    content = extract_indexable_content(data, fields)
    data = clean(content, tags=["br"], strip=True).strip()
    return data.split("<br>")[0]
