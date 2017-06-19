"""PyBird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from PyBirdApp import views

urlpatterns = [
    url(r'^$', views.start, name='start'), #Accueil PyBird
    url(r'^home', views.home, name='home'), #Accueil PyBird
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/(\d+)$', views.profile, name='profile'), #Page des post arg = id_user
    url(r'^followers/(\d+)$', views.followers, name='followers'), #Page des personnes qui suivent arg = id_user
    url(r'^followeds/(\d+)$', views.followeds, name='followeds'), #Page des que = id_user suit
]
