from django.contrib import admin
from .models import Recipes, Tag

# Register your models here.
admin.site.register(Recipes)
admin.site.register(Tag)