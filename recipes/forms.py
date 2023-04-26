from django import forms 
from django.forms import ModelForm
from django.forms.widgets import FileInput
from .models import Recipes

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'description', 'recipe_image', 'prep_time', 
                  'cook_time', 'serving', 'tags', 'instructions', 'ingredients']
        # To remove clear checkbox of ImageField from form use the following line
        # Here 'form-control-file' is a Bootstrap class
        widgets = {
            'recipe_image': FileInput(attrs={'class': 'form-control-file'}),
        }
     
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})   