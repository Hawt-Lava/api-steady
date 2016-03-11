from django.db import models

# Create your models here.


class Entry(models.Model):
    """An Entry refers to each input, there are multiple per spreadsheet"""
    score = models.IntegerField()

    class Meta:
        app_label = 'steady'
