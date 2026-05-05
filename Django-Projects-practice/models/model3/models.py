from django.db import models

class User(models.Model):
    name = models.CharField( max_length=50)
    username = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    create_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name
    
