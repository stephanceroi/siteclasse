from django.db import models
from django.contrib.auth.models import User, Group





class colleur(models.Model):
     
      user=models.OneToOneField(User, related_name='userc',on_delete=models.CASCADE, primary_key=True)
      matière=models.CharField(choices=(('M','Maths'),('P','Physique')), max_length=1, default='M')
      civilité=models.CharField(choices=(('M.',"Monsieur"),('Mme',"Madame")),max_length=3, default='M.')
      tel= models.CharField(max_length=20, blank=True, default='')
      def __str__(self):
          return self.civilité+" "+self.user.first_name+" "+self.user.last_name



class eleve(models.Model):
    user=models.OneToOneField(User, related_name='usere', on_delete=models.CASCADE, primary_key=True)
    photo = models.FileField(verbose_name="Trombine",
                      upload_to='trombi/',
                      max_length=255, null=True, blank=True)
    tel= models.CharField(max_length=20, blank=True, default='')
    civilité=models.CharField(choices=(('M.',"Monsieur"),('Mme',"Madame")),max_length=3, default='M.')
    def __str__(self):
          return self.civilité+" "+self.user.first_name+" "+self.user.last_name


# Create your models here.
class groupe(models.Model):
      nom=models.CharField(max_length=3, primary_key=True)
      el1=models.ForeignKey(eleve, on_delete=models.CASCADE, null=True, related_name='el1')
      el2=models.ForeignKey(eleve, on_delete=models.CASCADE, null=True, related_name='el2')
      el3=models.ForeignKey(eleve, on_delete=models.CASCADE, null=True, related_name='el3')

      def __str__(self):
          s=self.nom+" ("
          if self.el1 is None : s+="<vide>"
          else : 
                s+=self.el1.user.last_name
                if self.el2 is not None :
                      s+=", "+self.el2.user.last_name
                      if self.el3 is not None :
                            s+=", "+self.el3.user.last_name
          s+=")"
          return s #self.el1.user.last_name+','+self.el2.user.last_name+','+self.el3.user.last_name+')'
      def nombre(self):
          i=0
          if self.el1 is not None : i+=1
          if self.el2 is not None : i+=1
          if self.el3 is not None : i+=1
          return i

jours=[(1, 'lundi'), (2, 'mardi'), (3, 'mercredi'), (4, 'jeudi'), (
5, 'vendredi'), (6, 'samedi')]


class creneau(models.Model):
      jour=models.IntegerField(choices=jours, default=1)
      heure=models.IntegerField()
      colleur=models.ForeignKey(colleur, on_delete=models.CASCADE, null=True)
      duree=models.IntegerField(default=1)
      def __str__(self):
         return str(jours[self.jour-1][1])+" à "+str(self.heure)+"h avec "+str(self.colleur)
 
class colle(models.Model):
      id = models.AutoField(primary_key=True)
      semaine=models.IntegerField(default=1)
      creneau=models.ForeignKey(creneau, on_delete=models.CASCADE, null=True)
      groupe=models.ForeignKey(groupe, on_delete=models.CASCADE, null=True)
      note1=models.IntegerField(null=True)
      note2=models.IntegerField(null=True)
      note3=models.IntegerField(null=True)
      def __str__(self) :
            return str(self.id)+"sem."+str(self.semaine)+", gr. "+str(self.groupe)+str(self.note1)+"|"+str(self.note2)+"|"+str(self.note3)


class programme(models.Model):
      semaine=models.IntegerField(default=1)
      fichier=models.FileField(upload_to="programmes")
      
