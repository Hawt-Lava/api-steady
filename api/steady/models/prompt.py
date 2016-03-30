from django.db import models


class Prompt(models.Model):
    text = models.TextField()

    class Meta:
        app_label = 'steady'

    def __unicode__(self):
        """Returns text associated with the prompt"""
        return "{0}".format(self.text)
