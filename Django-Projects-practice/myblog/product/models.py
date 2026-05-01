from django.db import models

class product(models.model):
    prod_name = models.CharField(max_length=100)
    prod_descri = models.CharField(max_length=200)
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prod_name