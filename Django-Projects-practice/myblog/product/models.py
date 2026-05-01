from django.db import models

class product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_descri = models.CharField(max_length=200)
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
        return self.prod