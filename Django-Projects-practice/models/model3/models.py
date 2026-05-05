from django.db import models

class User(models.Model):
    name = models.CharField( max_length=50)
    username = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    create_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name
    
class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField()
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name
    