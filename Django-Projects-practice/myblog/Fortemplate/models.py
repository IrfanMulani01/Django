from django.db import models


class blog(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='blog/')

    def __str__(self):
        return self.name