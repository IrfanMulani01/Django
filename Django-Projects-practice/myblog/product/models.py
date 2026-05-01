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
    

class Prod_Details(models.Model):
    prod1 = models.OneToOneField(product, on_delete=models.CASCADE)
    prod_des = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.prod1.prod_name