from django.db import models


class FeedAlpha(models.Model):
    name = models.CharField(max_length=32)


class FeedBeta(models.Model):
    name = models.CharField(max_length=32)
