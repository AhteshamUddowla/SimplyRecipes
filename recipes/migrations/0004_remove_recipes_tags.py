# Generated by Django 4.0.4 on 2023-04-24 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipes_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='tags',
        ),
    ]
