from django.db import models

# Create your models here.


class Foo(models.Model):

    name = models.TextField()

    class Meta:
        app_label = 'steady'
