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
    nbpost, nbfollower, nbfollowed, listFollowed, posts = 0,0, 0, 0, 0


    if(request.user.is_authenticated()):
        nbpost = Post.objects.filter(id_author=request.user.id).count()
        nbfollower = Follow.objects.filter(id_followed=request.user.id).count()
        nbfollowed = Follow.objects.filter(id_follower=request.user.id).count()
        listFollowed = Follow.objects.filter(id_follower=request.user.id).all() # TODO : recuperer un tableau d'ID a la place d'un QuerySet<>

        if request.method == 'POST':
            content = request.POST.get('content', False)
            id_author = request.user
            p = Post.objects.create(post_content=content, id_author=id_author)
            p.save()

    list_user = User.objects.all() #Liste user contient la liste de tous les utilisateurs inscrits
    posts = Post.objects.order_by('-id').all()

    return render(request, 'PyBirdApp/index.html', {'nbpost': nbpost, 'nbfollower': nbfollower, 'nbfollowed': nbfollowed,
                                                    'list_user': list_user, 'listFollowed': listFollowed, 'posts' : posts})

def settings(request):
    if not request.user.is_authenticated: #Si l'user n'est pas authentifié
        return redirect('signup')

    return render(request, 'PyBirdApp/settings.html', {'date': datetime.now()}, format(request.user))

def profile(request, id_user):
    nbpost = Post.objects.filter(id_author = id_user).count()
    user = User.objects.filter(id=id_user)
    nbfollower = Follow.objects.filter(id_followed=id_user).count()
    nbfollowed = Follow.objects.filter(id_follower=id_user).count()
    isFollowed = Follow.objects.filter(id_follower=request.user.id, id_followed=id_user).count()
    post = Post.objects.order_by('-id').filter(id_author=id_user).all()

    if not user:
        raise Http404 #Pour renvoyer une erreur 404


    return render(request, 'PyBirdApp/profile.html', {'id_user': id_user, 'this_user': user, 'nbpost': nbpost,
                                                      'nbfollower': nbfollower, 'nbfollowed': nbfollowed, 'isFollowed': isFollowed,
                                                      'posts': post})


def followers(request, id_user):
    userFollowers = Follow.objects.filter(id_followed=id_user).all()
    user = User.objects.filter(id=id_user)

    if not user:
        raise Http404 #Pour renvoyer une erreur 404
    #recuperer les infos des mans a partir des id
    return render(request, 'PyBirdApp/followers.html', {'id_user': id_user, 'followers': userFollowers, 'this_user': user})

def followeds(request, id_user):
    userFollowers = Follow.objects.filter(id_follower=id_user).all()
    user = User.objects.filter(id=id_user)
    #recuperer les infos des mans a partir des id
    return render(request, 'PyBirdApp/followeds.html', {'id_user': id_user, 'followers': userFollowers, 'this_user': user})


def follow(request, id_user):
    if (not request.user.is_authenticated()):
        return redirect("signup") #Redirige l'user si il essaie de follow alors qu'il n'est pas connecté 

    user = User.objects.filter(id=id_user)

    if not user:
        raise Http404 #Pour renvoyer une erreur 404

    follow = Follow.objects.filter(id_follower=request.user.id, id_followed=id_user).count()

    if follow == 0:
        f = Follow.objects.create(id_follower=request.user.id, id_followed=id_user)
        f.save()

    if follow == 1:
        f = Follow.objects.filter(id_follower=request.user.id, id_followed=id_user)
        f.delete()

    tmp = request.META['HTTP_REFERER']
    return redirect(tmp)


