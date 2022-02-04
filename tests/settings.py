SECRET_KEY = "dump-secret-key"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.admin",
    "briefme_indexable_feed",
)

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

INDEXABLE_FEED_ACCESS_TOKEN = "test"

