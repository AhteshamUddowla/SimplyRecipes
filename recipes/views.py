from django.shortcuts import render, redirect
from .models import Recipes, Tag
from .forms import RecipeForm
from django.db.models import Q


# Create your views here.
def recipes(request):
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
    tags = Tag.objects.all()
    
    recipes = Recipes.objects.filter(
        Q(title__icontains=search) | 
        Q(description__icontains=search) 
    )
    
    context = {'recipes': recipes, 'tags':tags}
    return render(request, 'recipes/recipes.html', context)

def recipe(request, pk):
    recipe = Recipes.objects.get(id=pk)
    instructions = recipe.instructions.split('.')
    ingredients = recipe.ingredients.split('.')
    context = {'recipe': recipe, 'instructions':instructions, 
               'ingredients':ingredients}

    return render(request, 'recipes/recipe.html', context)    

def create_recipe(request):
    profile = request.user.profile
    form = RecipeForm()
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()
            return redirect('recipes')


    context = {'form':form}
    return render(request, 'recipes/recipe_form.html', context)


def edit_recipe_view(request, pk):
    profile = request.user.profile
    recipe = Recipes.objects.get(id=pk)
    form = RecipeForm(instance=recipe)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()
            return redirect('account')

    context = {'form':form}
    return render(request, 'recipes/recipe_form.html', context)


def delete_recipe_view(request, pk):
    recipe = Recipes.objects.get(id=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('account')

    context = {'recipe':recipe}
    return render(request, 'recipes/delete_form.html', context)


def tags_view(request):
    tags = Tag.objects.all()
    tag_count = []

    for tag in tags:
        tag_name = tag.name
        recipes = Recipes.objects.filter(
            Q(title__icontains=tag_name) | 
            Q(description__icontains=tag_name) 
        )
        tag_count.append(recipes.count())

    print(len(tag_count))
    print(len(tags))
    for tag, cn in zip(tags, tag_count):
        print(tag, cn)

    tag_list = zip(tags, tag_count)

    context = {'tags':tags, 'tag_count': tag_count, 'tag_list':tag_list}
    return render(request, 'recipes/tags.html', context)
