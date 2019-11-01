from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from colles.models import colleur,colle,creneau, eleve, programme
from colles.fonctions import *
#from colles.forms import essai
#from .forms import essai
#from django_ajax.decorators import ajax
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
#from datetime import deltatime, today

#exec(open('colles/fonctions.py').read())

@login_required
def colles(request):
    col=colleur.objects.filter(user=request.user)
    if len(col)!=0 :
        return colle_par_colleur(request)
    col=eleve.objects.filter(user=request.user)
    if len(col)!=0 :
        return colle_par_eleve(request)

def texte(c):
    if c is None : return ""
    if int(c)<0 : return "0"+str(c)
    return str(c)

    
def pdf_view(request,fichier):
    print(fichier)
    with open('programmes/'+fichier, 'rb') as pdf:
        #print(pdf.read())
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename='+fichier
    
        return response
    pdf.closed

def divers()  : #tableau des trucs en plus pour le bandeau gauche
    progs=programme.objects.order_by('semaine')
    dict={}
    print("longueur ",len(progs))
    t=[None for i in range(progs[len(progs)-1].semaine+1)]
    for e in progs :
        t[e.semaine]=e.fichier
    for i in range(len(t)-1,0,-1):
        dict[i]=t[i]
    print("divers", dict)
    return dict

    return HttpResponse()
def programmes(request):
    progs=programme.objects.order_by('sem')
    for e in progs :
        print(e)
    return HttpResponse()

def colloscope(request):
    return pdf_view(request, "colloscope.pdf")
    

@csrf_exempt
def entre_note(request):  #traitement de la requete ajax envoyée par le client
    c=request.POST.get("colle")
    note=request.POST.get("note")
    if note=="" : note=None
    else : note=int(note)
    print("note : ",note)
    
    print("user :", request.user)
    [idcol,nel]=c.split('|')  #numero du creneau et numero eleve
    nel=int(nel)
    print("colle : ",idcol)
    col=colle.objects.get(id=idcol)
    print(col.creneau.colleur)
    if   (col.creneau.colleur.user==request.user or request.user=="ceroi")\
    and nel>=1 and nel<=3 :
        if note==None or (note>=0 and note<=20) :
            if nel==1 : col.note1=note
            if nel==2 : col.note2=note
            if nel==3 : col.note3=note
            print("note modifiée", nel)
            print(col)
            col.save()
    return HttpResponse("toto")
@login_required
def colle_par_colleur(request):
    col=colleur.objects.get(user=request.user)
    print("colleur : ",col)
    sem=1  #la dernière semaine de colle
    while datelundi(sem)<date.today()+timedelta(days=6) :
        sem+=1
    
    nc=0
    s="<br>"
    tableau={}
    auj=datetime.today()
    while (sem>=1):
        cren=creneau.objects.filter(colleur=col)
        try :
            prog=programme.objects.get(semaine=sem)
        except :
            print("semaine", sem, "pdc absent")
            prog=None
        if prog!=None : print(prog.fichier.name)
        for cr in cren :
            try :
                c=colle.objects.get(semaine=sem,creneau=cr)
            except :
                print("semaine ",sem, "sans colle")
                
                break
            print("traitement semaine ", sem)
            s+=str(sem)+str(cr)+" "+str(c)+"<br>"
            nelvs=c.groupe.nombre()
            elvs={}
            if nelvs>=1 :
                
                elvs["1"]=[c.groupe.el1.user.last_name,texte(c.note1)]
            if nelvs>=2 :  
                elvs["2"]=[c.groupe.el2.user.last_name,texte(c.note2)]
            if nelvs>=3 :  
                elvs["3"]=[c.groupe.el3.user.last_name,texte(c.note3)]
        
                
            tableau['colle'+str(nc)]={'semaine':sem,'groupe':c.groupe.nom,\
            'date':jdaten(cr.jour,sem),'elvs':elvs, 'nelvs':nelvs, 'id':str(c.id)}
            if prog !=None :
                tableau['colle'+str(nc)]['prog']=prog.fichier.name
            #print(nc,tableau)
            nc+=1
        sem-=1
    print(tableau)
    return render(request, "colles/colleur.html", {'colleur' : str(col), 't1': tableau, 'divers':divers() })
    #return HttpResponse(str(col)+s)


def logout(request):
    return HttpReponse("Deconnexion réussie")
