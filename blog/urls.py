from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes', views.recipes, name='recipes'),
    path('recipes/<slug:recipe_slug>', views.recipe, name='recipe'),

    path('packages/', views.packages, name='packages'),
    path('packages/<int:package_id>', views.package, name='package'),

    path('foodpedia/', views.foodpedia, name='foodpedia'),
    path('foodpedia/<int:ingredient_id>', views.foodpedia_article, name='foodpedia_article'),

    path('value/', views.value, name='value'),

    path('blog/', views.blog, name='blog'),
    path('blog/<int:article_id>', views.blog_article, name='blog_post'),

    path('search', views.search_list, name='search')
]