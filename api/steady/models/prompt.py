from django.db import models
from entry import Entry


class Prompt(models.Model):
    text = models.TextField()
    entry = models.ForeignKey(Entry, related_name='prompt')
    class Meta:
        app_label = 'steady'

    def __unicode__(self):
        return "{0}".format(self.text)
