from django.db import models
from api.steady.models import Entry
from api.steady.models import User


class ScoreSheet(models.Model):
    """Holds onto a group of entries"""
    created = models.DateTimeField(auto_now=True)
    device_id = models.TextField()
    entries = models.ManyToManyField(Entry)

    class Meta:
        app_label = 'steady'
