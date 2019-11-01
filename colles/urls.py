from django.urls import path

from . import views

urlpatterns = [
    path('colles', views.colles, name='colles'),
    path('colleur', views.colle_par_colleur, name="colleur"),
    path(r'ajax/entrenote/',views.entre_note, name="entre_note"),
    path('programmes',views.programmes, name="programmes"),
    path('programmes/<str:fichier>',views.pdf_view, name="pdf_view"),
    path('colloscope', views.colloscope,name='colloscope'),
    #path('logout', views.logout,name='logout')
    ]
