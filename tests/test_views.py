import pytest

from django.conf import settings
from django.db import connection
from django.test.utils import CaptureQueriesContext
from rest_framework import serializers

from briefme_indexable_feed.views import BaseIndexableFeed
from tests.models import FeedAlpha, FeedBeta

pytestmark = pytest.mark.django_db


class FeedItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class DummyIndexableFeed(BaseIndexableFeed):
    queryset_list = [
        FeedAlpha.objects.all(),
        FeedBeta.objects.all(),
    ]
    serializer_classes = {
        FeedAlpha: FeedItemSerializer,
        FeedBeta: FeedItemSerializer,
    }


def _authenticated_path(**params):
    query = {"token": settings.INDEXABLE_FEED_ACCESS_TOKEN}
    query.update(params)
    return "/?" + "&".join(f"{key}={value}" for key, value in query.items())


class TestBaseIndexableFeed:
    def test_view_works_with_authentication(self, request_builder):
        # GIVEN
        request = request_builder.get(
            path=f"/?token={settings.INDEXABLE_FEED_ACCESS_TOKEN}"
        )

        # WHEN
        response = BaseIndexableFeed.as_view()(request)

        # THEN
        assert response.status_code == 200

    def test_view_raises_403_without_authentication(self, request_builder):
        # GIVEN
        request = request_builder.get()

        # WHEN
        response = BaseIndexableFeed.as_view()(request)

        # THEN
        assert response.status_code == 403
        assert (
            response.rendered_content.decode("utf-8")
            == '{"detail":"Authentication credentials were not provided."}'
        )

    def test_view_raises_exception_with_wrong_authentication(self, request_builder):
        # GIVEN
        request = request_builder.get(path="/?token=fake-token")

        # WHEN
        response = BaseIndexableFeed.as_view()(request)

        # THEN
        assert response.status_code == 403
        assert (
            response.rendered_content.decode("utf-8")
            == '{"detail":"The token value is wrong."}'
        )

    def test_page_two_does_not_fetch_page_one_rows(self, request_builder):
        # GIVEN
        FeedAlpha.objects.bulk_create(FeedAlpha(name=str(i)) for i in range(40))
        FeedBeta.objects.bulk_create(FeedBeta(name=str(i)) for i in range(10))
        request = request_builder.get(path=_authenticated_path(page=2))

        # WHEN
        with CaptureQueriesContext(connection) as captured:
            response = DummyIndexableFeed.as_view()(request)

        # THEN
        names = [row["name"] for row in response.data["results"]]
        assert response.data["count"] == 50
        assert names == [str(i) for i in range(30, 40)] + [str(i) for i in range(10)]
        selects = [
            query["sql"]
            for query in captured.captured_queries
            if "COUNT" not in query["sql"]
            and (
                "tests_feedalpha" in query["sql"] or "tests_feedbeta" in query["sql"]
            )
        ]
        assert selects
        assert all("LIMIT" in sql for sql in selects)
        assert any("OFFSET 30" in sql for sql in selects)
        assert any("ORDER BY" in sql for sql in selects)

    def test_page_size_is_capped_at_100(self, request_builder):
        # GIVEN
        FeedAlpha.objects.bulk_create(FeedAlpha(name=str(i)) for i in range(101))
        request = request_builder.get(path=_authenticated_path(page_size=10000))

        # WHEN
        response = DummyIndexableFeed.as_view()(request)

        # THEN
        assert response.data["count"] == 101
        assert len(response.data["results"]) == 100
        assert response.data["next"] is not None
