from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur PyBird !</h1>
              <p>Il s'agit d'un twitter like</p>"""
    return HttpResponse(text)

def view_post(request, id_post):
    """ 
    Vue qui affiche les posts selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    if int(id_post) > 10:
        raise Http404 #Pour renvoyer une erreur 404

        #return redirect("https://www.djangoproject.com") #Pour rediriger sur une autre page

    return HttpResponse(
        "Vous avez demandé le post #{0} !".format(id_post)
    )