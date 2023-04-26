from .models import Recipes, Tag
from django.db.models import Q

def searchRecipes(request):
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
    tags = Tag.objects.all()
    
    recipes = Recipes.objects.distinct().filter(
        Q(title__icontains=search) | 
        Q(description__icontains=search) |
        Q(tags__icontains=search)
    )

    return recipes, tags, search


def tagCount(request):
    tags = Tag.objects.all()
    tag_count = []

    for tag in tags:
        tag_name = tag.name
        recipes = Recipes.objects.distinct().filter(
            Q(title__icontains=tag_name) | 
            Q(description__icontains=tag_name) |
            Q(tags__icontains=tag_name)
        )
        tag_count.append(recipes.count())

    return tags, tag_count

def tags(request, recipe_tags):
    tag_list = []

    if recipe_tags:
        tag_list = recipe_tags.split(',')
        tag_list = [tag.strip().capitalize() for tag in tag_list]

    for tag in tag_list:
        Tag.objects.get_or_create(name=tag)
    
