from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def register_view(request):
    form = CustomUserCreationForm()

    if request.user.is_authenticated:
        return redirect('recipes')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes')

    context = {'form': form}
    return render(request, 'signup.html', context)

def login_view(request):

    if request.user.is_authenticated:
        return redirect('recipes')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username doesn't exists")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('recipes')
        else:
            messages.error(request, "Invalid Password")
    return render(request, 'signin.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def account_view(request):
    profile = request.user.profile
    recipes = profile.recipes_set.all()
    
    context = {'profile':profile, 'recipes':recipes}
    return render(request, 'users/account.html', context)

def edit_account_view(request, pk):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        username = request.POST['username']
        email = request.POST['email']

        if Profile.objects.filter(username=username).exists() and profile.username!=username:
            messages.error(request, 'Username already exists...')
        elif Profile.objects.filter(email=email).exists() and profile.email!=email:
            messages.error(request, 'Email already exists...')
        elif form.is_valid():
            user = form.save(commit=False)
            user.owner = profile
            user.save()
            return redirect('account')
    
    context = {'form':form}
    return render(request, 'users/edit-account.html', context )




