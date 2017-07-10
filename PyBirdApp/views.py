from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from PyBirdApp.models import Post, Follow
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def start(request):
    return render(request, 'PyBirdApp/start.html')

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
    nbpost, nbfollower, nbfollowed = 0, 0, 0

    if(request.user.is_authenticated()):
        nbpost = Post.objects.filter(id_author=request.user.id).count()
        nbfollower = Follow.objects.filter(id_followed=request.user.id).count()
        nbfollowed = Follow.objects.filter(id_follower=request.user.id).count()

    list_user = User.objects.all()

    return render(request, 'PyBirdApp/index.html', {'nbpost': nbpost, 'nbfollower': nbfollower, 'nbfollowed': nbfollowed,
                                                    'list_user': list_user})

def settings(request):
    if not request.user.is_authenticated: #Si l'user n'est pas authentifié
        return redirect('signup')

    return render(request, 'PyBirdApp/settings.html', {'date': datetime.now()}, format(request.user))

def profile(request, id_user):
    nbpost = Post.objects.filter(id_author = id_user).count()
    user = User.objects.filter(id=id_user)
    nbfollower = Follow.objects.filter(id_followed=id_user).count()
    nbfollowed = Follow.objects.filter(id_follower=id_user).count()

    if not user:
        raise Http404 #Pour renvoyer une erreur 404

    if(request.user.id == id_user):
        myPage = 1
    else:
        myPage = 0

    return render(request, 'PyBirdApp/profile.html', {'id_user': id_user, 'this_user': user, 'nbpost': nbpost, 'myPage': myPage,
                                                      'nbfollower': nbfollower, 'nbfollowed': nbfollowed})


def followers(request, id_user):
    return render(request, 'PyBirdApp/followers.html', {'id_user': id_user})

def follow(request, id_user):
    follow = Follow.objects.filter(id_follower=request.user.id, id_followed=id_user).count()

    if follow < 0:
        return redirect("http://google.com")

    return render(request, 'PyBirdApp/followers.html', {'id_user': id_user})

def followeds(request, id_user):
    return render(request, 'PyBirdApp/followeds.html', {'id_user': id_user})


