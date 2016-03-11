from django.db import models
from api.steady.models import Entry


class ScoreSheet(models.Model):
    """Holds onto a group of entries"""
    created = models.DateTimeField(auto_now=True)
    label = models.TextField()
    entries = models.ForeignKey(Entry)

    class Meta:
        app_label = 'steady'
