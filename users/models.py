from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, 
                    upload_to='profiles/', default='profiles/user_default.png')
    bio = models.TextField(max_length=2000, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)
