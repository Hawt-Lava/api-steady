from django.db import models
from prompt import Prompt

# Create your models here.


class Entry(models.Model):
    """An Entry refers to each input, there are multiple per spreadsheet"""
    score = models.IntegerField()
    prompt = models.ForeignKey(Prompt, default=1)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'steady'
