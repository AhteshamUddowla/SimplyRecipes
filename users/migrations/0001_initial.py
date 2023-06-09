# Generated by Django 4.0.4 on 2023-04-23 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('username', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, max_length=2000, null=True)),
                ('profile_image', models.ImageField(blank=True, default='profiles/user_default.png', null=True, upload_to='profiles/')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
