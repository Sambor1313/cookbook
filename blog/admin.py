from django.contrib import admin

from .models import Unit, Ingredient, Recipe, Kitchenware, IngredientsList, Package, BlogPost

# Register your models here.
class UnitAdmin(admin.ModelAdmin):
    fields = ['name', 'symbol']
    list_display = ('name', 'symbol')

admin.site.register(Unit, UnitAdmin)

class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Ingredient, IngredientAdmin)

class IngredientsListInline(admin.TabularInline):
    model = IngredientsList
    extra = 5
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [IngredientsListInline]

admin.site.register(Recipe, RecipeAdmin)

class KitchenwareAdmin(admin.ModelAdmin):
    pass

admin.site.register(Kitchenware, KitchenwareAdmin)


class PackageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Package, PackageAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'author')

admin.site.register(BlogPost, BlogPostAdmin)