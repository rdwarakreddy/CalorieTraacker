from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()#Calories
    Proteins = models.FloatField()#proteins
    fats = models.FloatField()#fats
    Carbohydrates = models.FloatField()#carbohydrates
    # category = models.CharField(max_length=200)
    description = models.TextField()
    Image = models.CharField(max_length=1000)#storing image URL
    def __str__(self):
        return self.title
class Orders(models.Model):
    items = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    totalquantity = models.IntegerField(max_length=100)
    totalcost = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name