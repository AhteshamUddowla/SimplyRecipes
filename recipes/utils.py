from .models import Recipes, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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


def pagination(request, recipes):
    paginator = Paginator(recipes, 3)
    page = request.GET.get('page')

    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        recipes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        recipes = paginator.page(page)

    leftIndex = int(page)-2

    if(leftIndex < 1):
        leftIndex = 1

    rightIndex = int(page)+3

    if(rightIndex > paginator.num_pages):
        rightIndex = paginator.num_pages+1

    if int(page)>=1 and int(page)<=2 and paginator.num_pages>=5:
        rightIndex=6
    if int(page)>paginator.num_pages-2 and paginator.num_pages>=5:
        leftIndex=paginator.num_pages-4

    custom_range = range(leftIndex, rightIndex)

    return recipes, custom_range


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
    
