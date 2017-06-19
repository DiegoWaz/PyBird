from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
from datetime import datetime

#def date_actuelle(request):
#    return render(request, 'PyBirdApp/date.html', {'date': datetime.now(), 'jour': "Mardi", 'mot' : "salut"})


#def addition(request, nombre1, nombre2):
#    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
#    return render(request, 'PyBirdApp/addition.html', locals())

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