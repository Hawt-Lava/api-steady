from django.db import models

# Create your models here.


class Prompt(models.Model):
    text = models.TextField()
