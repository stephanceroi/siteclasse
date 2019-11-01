from datetime import *

def enleve_accents(ligne):
    accent =      ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
    for c, s in zip(accent, sans_accent):
            ligne = ligne.replace(c, s)
    return ligne

def loginDeNom(nom):
   login=nom.lower()
   login=enleve_accents(login.split("-")[0])
   return login 

def datelundi(sem):
    """rend la date du lundi de la n-ieme semaine de colle
    au format datetime"""
    semaines=["23/09/19","30/09/19","07/10/19","14/10/19","04/11/19","11/11/19","18/11/19","25/11/19","02/12/19","09/12/19","16/12/19","06/01/20","13/01/20","20/01/20"]
    s=semaines[sem-1]
    s=s.split('/')
    jour=int(s[0])
    mois=int(s[1])
    annee=int(s[2])+2000
    return date(annee, mois, jour)

jourdelasem=['Lundi','Mardi','Mercredi','Jeudi','Vendredi']
    

def jdate(njour,s):
    """njour est "Lundi" ou "Mardi" etc.., rend la date
du jour correspondant de la semaine de colle s"""
    global j
    d=datelundi(s)+timedelta(days=(j.index(njour)))
    return njour+" "+str(d.day)+"/"+str(d.month)+"/"+str(d.year-2000)

def jdaten(njour,s):
    """njour est "1" ou "2" etc.., rend la date
du jour correspondant de la semaine de colle s"""
    d=datelundi(s)+timedelta(days=njour-1)
    return str(d.day)+"/"+str(d.month)+"/"+str(d.year-2000)



