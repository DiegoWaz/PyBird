from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from PyBirdApp.models import Post
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def start(request):
    return render(request, 'PyBirdApp/start.html', {'date': datetime.now()})

def user_login(request):
    if request.method == 'POST':
            username = request.POST.get('username', False)
            password = request.POST.get('password', False)
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('home')

    return render(request, 'PyBirdApp/registration/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'PyBirdApp/registration/signup.html', {'form': form})


def user_logout(request):
    logout(request)

    return redirect('home')

def home(request):
    return render(request, 'PyBirdApp/index.html', {'date': datetime.now()})

def settings(request):
    if not request.user.is_authenticated: #Si l'user n'est pas authentifié
        return redirect('signup')

    return render(request, 'PyBirdApp/settings.html', {'date': datetime.now()}, format(request.user))

def profile(request, id_user):
    post = Post.objects.all()  # Nous sélectionnons tous nos posts
    user = User.objects.filter(id=id_user)  # Nous sélectionnons l'user courant

    if not user:
        raise Http404 #Pour renvoyer une erreur 404

    return render(request, 'PyBirdApp/profile.html', {'this_user': user})


def followers(request, id_user):
    return render(request, 'PyBirdApp/followers.html', {'id_user': id_user})

def followeds(request, id_user):
    return render(request, 'PyBirdApp/followeds.html', {'id_user': id_user})


