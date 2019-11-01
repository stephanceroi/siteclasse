from django.contrib.auth.models import User, Group
from colles.models import *
from datetime import *

from  colles.fonctions import *
# à executer dans le shell de l'application:
# >python3 manage.py shell
# puis dans Ipython:
# exec(open('init.py').read())


"""colleurs=Group(name="Colleurs")
colleurs.save()

eleves=Group(name="Élèves")
eleves.save()

"""
#colleurs=Group.objects.get(name='Colleurs')
#eleves=Group.objects.get(name='Élèves')


#------------creation des colleurs 

u=User.objects.create_user('bonvalot', 'laurence.bonvalot@wanadoo.fr', 'ppccssii', first_name="Laurence", last_name="Bonvalot" )
#u.groups.add(colleurs)
u=colleur(user=u,civilité="Mme")
u.save()

u=User.objects.create_user('schmitt', 'isabelle.schmitt.guillou@gmail.com', 'ppccssii', first_name="Isabelle", last_name="Schmitt" )
#u.groups.add(colleurs)
u=colleur(user=u,civilité="Mme")
u.save()

u=User.objects.create_user('helsly', 'yannick.helsly@gmail.com', 'ppccssii', first_name="Yannick", last_name="Helsly" )
#u.groups.add(colleurs)
u=colleur(user=u,civilité="M.")
u.save()

u  = User.objects.get(username="ceroi")
#u.groups.add(colleurs)
u=colleur(user=u,civilité="M.")
u.save()


#----------------Creation eleves

i=0
LE=[]
f=open("ListeEleves2019.csv", "r")
for ligne in f :
    l=ligne.split(',')
    nom=l[1] 
    login=loginDeNom(nom)
    LE.append([nom,login])
    print(l[1],login)     
    u=User.objects.create_user(login,l[3],l[1])
    u.first_name=l[2]
    u.last_name=l[1]
    #u.groups.add(eleves)
    u.save()
    u=eleve(user=u,civilité=l[0])
    u.save()
f.close()

#         traitement des groupes

f=open("groupes.csv")
for ligne in f:
    l=ligne.split(',')
    gr=l[0][6:].strip()  #on saute "Groupe"
    g=groupe(nom=gr)
    
    if l[2]!="" :
        l[2]=l[2].split(' ')[0]
        login=loginDeNom(l[2])
        print(l[2],login)
        u=User.objects.filter(username=login)[0]
        g.el1=eleve.objects.filter(user=u)[0]
    if l[3]!="" :
        l[3]=l[3].split(' ')[0]
        login=loginDeNom(l[3])
        print(l[3],login)
        u=User.objects.filter(username=login)[0]
        g.el2=eleve.objects.filter(user=u)[0]
    if l[4]!="" :
        l[4]=l[4].split(' ')[0]
        login=loginDeNom(l[4])
        print(l[4],login)
        u=User.objects.filter(username=login)[0]
        print(u)
        g.el3=eleve.objects.filter(user=u)[0]
    print(g.nombre())
    print(g)
    g.save()


#---------------------------------------
#  remplissage des colles 
fichier=open("collo.csv",'r')
for ligne in fichier :
    lig=ligne.split(',')
    if lig[1]=='' :
        matiere=lig[0]
        print("matiere : ",matiere)
    else :
        logcol=loginDeNom(lig[0].split(' ')[1])
        print(logcol)
        u=User.objects.filter(username=logcol)[0]
        col=colleur.objects.filter(user=u)[0]
        print(col.user.first_name)
        cr=lig[1].split(' ')
        jour=j.index(cr[0])+1
        heure=int(cr[1][:2])
        print("jour:",jour, heure)
        cr=creneau(jour=jour,heure=heure,colleur=col)
        cr.save()
        salle=lig[3]
        grs=lig[3:]
        #lig.insert(0,matiere)
        #print(lig)
        print("**************",creneau)
        for nsem in range(len(grs)) :
            print("groupe : '"+grs[nsem].strip()+"'")
            if grs[nsem]!="" :
                g=groupe.objects.filter(nom=grs[nsem].strip())[0]
                print(g)
                c=colle(semaine=nsem+1,creneau=cr,groupe=g)
                c.save()
    
