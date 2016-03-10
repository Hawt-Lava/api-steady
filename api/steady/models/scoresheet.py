from django.db import models
from models.entry import Entry
# Create your models here.


class ScoreSheet(models.Model):
    """Holds onto a group of entries"""
    date = models.TimeField()
    entries = models.ForeignKey(Entry, many=True)
