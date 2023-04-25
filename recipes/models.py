from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Recipes(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, null=True, blank=True)
    recipe_image = models.ImageField(null=True, blank=True,
                   upload_to='recipes/', default='recipes/recipe_default.png')
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    serving = models.IntegerField()
    instructions = models.TextField(max_length=5000)
    ingredients = models.TextField(max_length=5000)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name