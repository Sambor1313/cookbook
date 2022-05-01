from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from blog.models import BlogPost

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', context={})

def recipes(request):
    return render(request, 'blog/recipes.html', context={'test': ["a", "b", "c"]})

def recipe(request, recipe_id):
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
    return render(request, 'blog/value.html', context={})

def blog(request):
    blog_list = BlogPost.objects.filter(publish_date__isnull=False).order_by('-publish_date')
    paginator = Paginator(blog_list, 1)
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

