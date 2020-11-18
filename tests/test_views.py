import pytest

from briefme_indexable_feed.views import BaseIndexableFeed

pytestmark = pytest.mark.django_db


class TestBaseIndexableFeed:
    def test_view_works(self, request_builder):
        # GIVEN
        request = request_builder.get()

        # WHEN
        response = BaseIndexableFeed.as_view()(request)

        # THEN
        assert response.status_code == 200
