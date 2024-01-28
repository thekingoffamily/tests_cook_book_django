from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    times_cooked = models.IntegerField(default=0)

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, through='RecipeProduct')

class RecipeProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.IntegerField()