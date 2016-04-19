from django.db import models

class User(models.Model):
    device_id = models.TextField()

    class Meta:
        app_label = 'steady'
