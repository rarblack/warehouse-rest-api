from django.db import models


class FCMModel(models.Model):
    token = models.CharField(max_length=400)

    def __str__(self):
        return self.token
