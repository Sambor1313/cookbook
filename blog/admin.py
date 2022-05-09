from textwrap import shorten
from django.contrib import admin
from django.utils.html import format_html

from .models import Unit, Ingredient, Recipe, Kitchenware, IngredientsList, Package, BlogPost, Tag

# Register your models here.
class UnitAdmin(admin.ModelAdmin):
    fields = ['name', 'symbol']
    list_display = ('name', 'symbol')
    search_fields = [
        'name',
        'symbol'
    ]

admin.site.register(Unit, UnitAdmin)

class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug','get_description')

    def get_description(self, obj):
        return shorten(obj.content, width=55, placeholder='...', break_long_words=False)

    search_fields = [
        'name',
        'content'
    ]

admin.site.register(Ingredient, IngredientAdmin)

class IngredientsListInline(admin.TabularInline):
    model = IngredientsList
    extra = 5
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display=('name', 'content')
    search_fields = [
        'name',
        'content'
    ]
    inlines = [IngredientsListInline]

admin.site.register(Recipe, RecipeAdmin)

class KitchenwareAdmin(admin.ModelAdmin):
    list_display=('name', 'get_description')
    search_fields = [
        'name',
        'content'
    ]
    def get_description(self, obj):
        return shorten(obj.content, width=78, placeholder='...', break_long_words=False)

admin.site.register(Kitchenware, KitchenwareAdmin)


class PackageAdmin(admin.ModelAdmin):
    search_fields = [
        'name'
    ]

admin.site.register(Package, PackageAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'author', 'tags_list')
    list_filter = [
        'author',
        'publish_date'
    ]
    search_fields = [
        'title'
    ]

    def filtered_tags(self):
        return Tag.objects.filter(type_tag=Tag.BLOG)

admin.site.register(BlogPost, BlogPostAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type_tag', 'get_color')
    def get_color(self, obj):
        return format_html(
            '<div style="background-color: {}; width: 50px;">&nbsp;</div>',
            obj.color
        )
    
    list_filter = [
        'type_tag',
        'color'
    ]
    search_fields = [
        'name',
        'description'
    ]

admin.site.register(Tag, TagAdmin)