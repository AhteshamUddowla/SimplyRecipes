from django.forms.widgets import FileInput
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # make the email field required
    
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name':'Name',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your name...','autofocus': True}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email...',}),
            'password1': forms.PasswordInput(attrs={'placeholder': '••••••••••••••••'}),
            'password2': forms.PasswordInput(attrs={'placeholder': '••••••••••••••••'}),
        }

    # If an email address already exist gives an validation error
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'profile_image', 'bio']
        # To remove clear checkbox of ImageField from form use the following line
        # Here 'form-control-file' is a Bootstrap class
        widgets = {
            'profile_image': FileInput(attrs={'class': 'form-control-file'}),
            'bio': forms.TextInput(attrs={'style': 'border: 1px solid #ccc;'}),
        }