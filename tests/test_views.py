import pytest

from django.conf import settings

from briefme_indexable_feed.views import BaseIndexableFeed

pytestmark = pytest.mark.django_db


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
