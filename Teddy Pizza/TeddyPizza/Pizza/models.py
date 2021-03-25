
# Create your models here.
from django.db import models

# Create your models here.
class Pizza(models.Model):
    CustomerName = models.CharField(max_length=50, default="")
    pizza_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50, default="")

class IngredientList(models.Model):
    ingredient_name = models.CharField(max_length=50, primary_key = True)
    supplier_name = models.CharField(max_length=50)


