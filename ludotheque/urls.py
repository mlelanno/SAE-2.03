from django.urls import path
from . import views

urlpatterns = [
    path('auteurs/', views.liste_auteurs, name='liste_auteurs'),
    path('auteurs/ajouter/', views.ajouter_auteur, name='ajouter_auteur'),
]