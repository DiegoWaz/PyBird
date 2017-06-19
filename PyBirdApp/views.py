from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from datetime import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

#def date_actuelle(request):
#    return render(request, 'PyBirdApp/date.html', {'date': datetime.now(), 'jour': "Mardi", 'mot' : "salut"})


#def addition(request, nombre1, nombre2):
#    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
#    return render(request, 'PyBirdApp/addition.html', locals())

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

def profile(request, id_user):
    """ 
    Vue qui affiche les posts selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    if int(id_user) > 10:
        raise Http404 #Pour renvoyer une erreur 404

        #return redirect("https://www.djangoproject.com") #Pour rediriger sur une autre page

    return render(request, 'PyBirdApp/profile.html', {'id_user': id_user})

def followers(request, id_user):
    return render(request, 'PyBirdApp/followers.html', {'id_user': id_user})

def followeds(request, id_user):
    return render(request, 'PyBirdApp/followeds.html', {'id_user': id_user})