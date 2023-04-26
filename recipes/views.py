from django.shortcuts import render, redirect
from .models import Recipes, Tag
from .forms import RecipeForm
from .utils import searchRecipes, tagCount, tags
from django.contrib.auth.decorators import login_required

# Create your views here.
def recipes(request):
    recipes, tags, search = searchRecipes(request)
    
    context = {'recipes': recipes, 'tags':tags, 'search':search}
    return render(request, 'recipes/recipes.html', context)

def recipe(request, pk):
    recipe = Recipes.objects.get(id=pk)

    tags = []
    if recipe.tags:
        tags = recipe.tags.split(',')
        tags = [tag.strip() for tag in tags]
    tags = set(tags)

    instructions = recipe.instructions.split('.')
    ingredients = recipe.ingredients.split('.')
    context = {'recipe': recipe, 'instructions':instructions, 
               'ingredients':ingredients, 'tags':tags}

    return render(request, 'recipes/recipe.html', context)    

@login_required(login_url='login')
def create_recipe(request):    
    profile = request.user.profile
    form = RecipeForm()
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()
            tags(request, recipe.tags)
            return redirect('recipes')


    context = {'form':form}
    return render(request, 'recipes/recipe_form.html', context)

@login_required(login_url='login')
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
            tags(request, recipe.tags)
            
            return redirect('account')

    context = {'form':form}
    return render(request, 'recipes/recipe_form.html', context)

@login_required(login_url='login')
def delete_recipe_view(request, pk):
    recipe = Recipes.objects.get(id=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('account')

    context = {'recipe':recipe}
    return render(request, 'recipes/delete_form.html', context)


def tags_view(request):
    tags, tag_count = tagCount(request)

    tag_list = zip(tags, tag_count)

    context = {'tags':tags, 'tag_count': tag_count, 'tag_list':tag_list}
    return render(request, 'recipes/tags.html', context)
