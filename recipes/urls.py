from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('recipe/<str:pk>/', views.recipe, name='recipe'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),

    path('edit-recipe/<str:pk>/', views.edit_recipe_view, name='edit-recipe'),
    path('delete-recipe/<str:pk>/', views.delete_recipe_view, name='delete-recipe'),

    path('tags/', views.tags_view, name='tags'),
]

