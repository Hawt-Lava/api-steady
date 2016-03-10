from django.db import models
from models.prompt import Prompt
# Create your models here.


class Entry(models.Model):
    """An Entry refers to each input, there are multiple per spreadsheet"""
    score = models.IntegerField()
    prompt = models.ForeignKey(Prompt, related_name='prompt')
