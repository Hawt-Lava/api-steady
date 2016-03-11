from django.db import models
from api.steady.models import Entry


class ScoreSheet(models.Model):
    """Holds onto a group of entries"""
    created = models.DateTimeField(auto_now_add=True)
    entries = models.ForeignKey(Entry)

    class Meta:
        app_label = 'steady'
