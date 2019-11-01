from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render
from colles.models import *
#from django.contrib.auth.models import User, Group


def accueil(request):
    
    u=request.user
    for g in u.groups.all():
       print(g.name)
        
    return HttpResponse("Accueil "+request.user.first_name)



def groupe(request,gn): #affiche les eleves du groupe de nom gn
    el=eleve.objects.filter(groupe=gn) 
    if len(el)==0 : return HttpResponse("Ce groupe est inconnu ou vide")
    sel=""
    for e in el :
        sel+="<br>"+str(e)

    return HttpResponse("on va voir le groupe "+gn +" : "+sel)


def logout(request):
    print("toto")
    return HttpResponse("Déconnexion réussie")

