from django.db import models

# Create your models here.


class ScoreSheet(models.Model):
    """Holds onto a group of entries"""
    date = models.TimeField()
