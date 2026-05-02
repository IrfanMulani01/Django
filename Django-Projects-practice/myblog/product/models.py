from django.db import models

class product(models.Model):
    prod_name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prod_name
    


        ######  one - to  - many relationship   ######

class Prod_review(models.Model):
    prod = models.ForeignKey(product, on_delete=models.CASCADE)
    review = models.IntegerField()
    com = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prod.prod_name
    

    #####   one to one relationship     ######

class User_profile(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    user_name = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname
  

            ######  many - to - many realationship  #######
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)