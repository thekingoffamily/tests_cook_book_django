from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from .models import Product, Recipe, RecipeProduct
from django.core import serializers

def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)

    recipe_product, created = RecipeProduct.objects.get_or_create(
        recipe=recipe, product=product, defaults={'weight': weight})

    if not created:
        recipe_product.weight = weight
        recipe_product.save()

    data = {
        'recipe_id': recipe.id,
        'recipe_name': recipe.name,
        'product_id': product.id,
        'product_name': product.name,
        'weight': recipe_product.weight,
        'created': created
    }
    return JsonResponse(data)

def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    for product in recipe.products.all():
        product.times_cooked += 1
        product.save()

    recipe_data = serializers.serialize('json', [recipe])
    return HttpResponse(recipe_data, content_type="application/json")

def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)

    recipes = Recipe.objects.exclude(products=product)
    recipes_data = serializers.serialize('json', recipes)

    return HttpResponse(recipes_data, content_type="application/json")
