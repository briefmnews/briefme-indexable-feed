from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

User = get_user_model()


class QueryStringAuthentication(BaseAuthentication):
    """Custom authentication with query string token"""

    def authenticate(self, request):
        token = request.GET.get("token", None)
        if token:
            if token == settings.INDEXABLE_FEED_ACCESS_TOKEN:
                return User(), None
            else:
                raise exceptions.AuthenticationFailed("The token value is wrong.")

        return None
