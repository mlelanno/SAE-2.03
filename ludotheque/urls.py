from django.urls import path
from . import views

urlpatterns = [
    # Routes pour la gestion des Auteurs
    path('auteurs/', views.liste_auteurs, name='liste_auteurs'),
    path('auteurs/ajouter/', views.ajouter_auteur, name='ajouter_auteur'),
    path('auteurs/modifier/<int:id>/', views.modifier_auteur, name='modifier_auteur'),
    path('auteurs/supprimer/<int:id>/', views.supprimer_auteur, name='supprimer_auteur'),

    # THE NEW HOME ROUTE
    path('', views.home, name='home'),

    # Keep all your existing routes below this line...
    path('jeux/', views.liste_jeux, name='liste_jeux'),
    path('jeux/ajouter/', views.ajouter_jeu, name='ajouter_jeu'),
    # ... (rest of your routes)

    # Routes pour la gestion des Catégories
    path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('categories/modifier/<int:id>/', views.modifier_categories, name='modifier_categories'),
    path('categories/supprimer/<int:id>/', views.supprimer_categories, name='supprimer_categories'),

    # Routes pour la gestion des Jeux
    path('jeux/', views.liste_jeux, name='liste_jeux'),
    path('jeux/ajouter/', views.ajouter_jeu, name='ajouter_jeu'),
    path('jeux/modifier/<int:id>/', views.modifier_jeu, name='modifier_jeu'),
    path('jeux/supprimer/<int:id>/', views.supprimer_jeu, name='supprimer_jeu'),

    # Routes pour la gestion des Joueurs
    path('joueurs/', views.liste_joueurs, name='liste_joueurs'),
    path('joueurs/ajouter/', views.ajouter_joueur, name='ajouter_joueur'),
    path('joueurs/modifier/<int:id>/', views.modifier_joueur, name='modifier_joueur'),
    path('joueurs/supprimer/<int:id>/', views.supprimer_joueur, name='supprimer_joueur'),

    # Routes pour la gestion des Commentaires
    path('commentaires/', views.liste_commentaires, name='liste_commentaires'),
    path('commentaires/ajouter/', views.ajouter_commentaire, name='ajouter_commentaire'),
    path('commentaires/modifier/<int:id>/', views.modifier_commentaire, name='modifier_commentaire'),
    path('commentaires/supprimer/<int:id>/', views.supprimer_commentaire, name='supprimer_commentaire'),

    path('jeux/<int:id>/details/', views.detail_jeu, name='detail_jeu'),
]