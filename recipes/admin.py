from django.contrib import admin
from .models import Product, Recipe

class RecipeProductInline(admin.TabularInline):
    model = Recipe.products.through

class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipeProductInline,
    ]
    exclude = ('products',)

admin.site.register(Product)
admin.site.register(Recipe, RecipeAdmin)