from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings

from blog.models import BlogPost, Recipe, Package

# Home Page
def index(request):
    # Get three of random recipes
    recipe_list = Recipe.objects.order_by('?')[:3]

    # Get one random blogPost
    blog_post = BlogPost.objects.order_by('?').first()

    # Get one random package
    package_random = Package.objects.order_by('?').first()

    # Get one random foodpedia article
    foodpedia_article = {
        'name': 'Test - article'
    }


    return render(request, 'blog/index.html', context={
        'recipe_list': recipe_list,
        'package_random': package_random,
        'foodpedia_article': foodpedia_article,
        'blog_post': blog_post
    })

# Recipes - list of recipe with filters
def recipes(request):
    recipe_list = Recipe.objects.all()
    paginator = Paginator(recipe_list, settings.PAGINATION)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/recipes.html', context={
        'page_obj': page_obj,
        'filters': True
    })

def recipe(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    return render(request, 'blog/recipe.html', context={
        'recipe': recipe,
        'ingredinets': recipe.ingredients.through.objects.all(),
        'steps':[t.strip() for t in recipe.instructions.split(';')],
        'filters': True
    })
    return render(request, 'blog/recipe.html', context={})

def packages(request):
    return render(request, 'blog/packages.html', context={})

def package(request, package_id):
    return render(request, 'blog/package.html', context={})

def foodpedia(request):
    return render(request, 'blog/foodpedia.html', context={})

def foodpedia_article(request, ingredient_id):
    return render(request, 'blog/foodpedia_article.html', context={})

def value(request):
    return render(request, 'blog/value.html')

def blog(request):
    blog_list = BlogPost.objects.filter(publish_date__isnull=False).order_by('-publish_date')
    paginator = Paginator(blog_list, settings.PAGINATION)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', context={
        'page_obj': page_obj,
        'filters': True
    })

def blog_article(request, article_id):
    blog_post = get_object_or_404(BlogPost, pk=article_id)
    return render(request, 'blog/blog_article.html', context={
        'blog_post': blog_post,
        'filters': True
    })

def search_list(request, fraze):
    return render(request, 'blog/search_list.html', context={})

