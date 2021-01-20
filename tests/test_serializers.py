import pytest

from briefme_indexable_feed.serializers import get_indexable_content

pytestmark = pytest.mark.django_db


class TestExtractIndexableCotent:
    def test_with_json_data(self, data):
        # GIVEN
        fields = ["title", "text"]

        # WHEN
        response = get_indexable_content(data, fields)

        # THEN
        assert "<p>" not in response
