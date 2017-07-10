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
    return render(request, 'PyBirdApp/signup.html', {'form': form})

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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('PyBirdApp/login')

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('PyBirdApp/home')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return redirect('PyBirdApp/singup.html', {}, context)
