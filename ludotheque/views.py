import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Auteur, Categorie, Jeu, Joueur, Commentaire
from .forms import AuteurForm, CategorieForm, JeuForm, JoueurForm, CommentaireForm

# ==========================================
# VIEW POUR LE DASHBOARD (HOME)
# ==========================================

def home(request):
    # Querying the database for aggregate metrics
    stats = {
        'total_jeux': Jeu.objects.count(),
        'total_categories': Categorie.objects.count(),
        'total_auteurs': Auteur.objects.count(),
        'total_joueurs': Joueur.objects.count()
    }
    return render(request, 'ludotheque/home.html', {'stats': stats})

# ==========================================
# VIEWS POUR LE MODELE : AUTEUR
# ==========================================

def liste_auteurs(request):
    auteurs = Auteur.objects.all()
    return render(request, 'ludotheque/liste_auteurs.html', {'auteurs': auteurs})

def ajouter_auteur(request):
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'auteur a été ajouté avec succès.")
            return redirect('liste_auteurs')
    else:
        form = AuteurForm()
    return render(request, 'ludotheque/ajouter_auteur.html', {'form': form})

def modifier_auteur(request, id):
    auteur = get_object_or_404(Auteur, id=id)
    if request.method == 'POST':
        form = AuteurForm(request.POST, instance=auteur)
        if form.is_valid():
            form.save()
            messages.success(request, "Les informations de l'auteur ont été mises à jour.")
            return redirect('liste_auteurs')
    else:
        form = AuteurForm(instance=auteur)
    return render(request, 'ludotheque/modifier_auteur.html', {'form': form, 'auteur': auteur})

def supprimer_auteur(request, id):
    auteur = get_object_or_404(Auteur, id=id)
    if request.method == 'POST':
        auteur.delete()
        messages.success(request, "L'auteur a été supprimé de la base de données.")
        return redirect('liste_auteurs')
    return render(request, 'ludotheque/supprimer_auteur.html', {'auteur': auteur})


# ==========================================
# VIEWS POUR LE MODELE : CATEGORIE
# ==========================================

def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'ludotheque/liste_categories.html', {'categories': categories})

def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La catégorie a été ajoutée avec succès.")
            return redirect('liste_categories')
    else:
        form = CategorieForm()
    return render(request, 'ludotheque/ajouter_categorie.html', {'form': form})

def modifier_categories(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            messages.success(request, "La catégorie a été mise à jour.")
            return redirect('liste_categories')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'ludotheque/modifier_categorie.html', {'form': form, 'categorie': categorie})

def supprimer_categories(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        categorie.delete()
        messages.success(request, "La catégorie a été supprimée.")
        return redirect('liste_categories')
    return render(request, 'ludotheque/supprimer_categorie.html', {'categorie': categorie})


# ==========================================
# VIEWS POUR LE MODELE : JEU
# ==========================================

def liste_jeux(request):
    jeux = Jeu.objects.select_related('auteur', 'categorie').all()
    return render(request, 'ludotheque/liste_jeux.html', {'jeux': jeux})

def ajouter_jeu(request):
    if request.method == 'POST':
        form = JeuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le jeu a été ajouté au catalogue avec succès.")
            return redirect('liste_jeux')
    else:
        form = JeuForm()
    return render(request, 'ludotheque/ajouter_jeu.html', {'form': form})

def modifier_jeu(request, id):
    jeu = get_object_or_404(Jeu, id=id)
    if request.method == 'POST':
        form = JeuForm(request.POST, instance=jeu)
        if form.is_valid():
            form.save()
            messages.success(request, f"Les informations de '{jeu.titre}' ont été mises à jour.")
            return redirect('liste_jeux')
    else:
        form = JeuForm(instance=jeu)
    return render(request, 'ludotheque/modifier_jeu.html', {'form': form, 'jeu': jeu})

def supprimer_jeu(request, id):
    # This is the function that was accidentally deleted!
    jeu = get_object_or_404(Jeu, id=id)
    if request.method == 'POST':
        nom_jeu = jeu.titre
        jeu.delete()
        messages.success(request, f"Le jeu '{nom_jeu}' a été définitivement supprimé.")
        return redirect('liste_jeux')
    return render(request, 'ludotheque/supprimer_jeu.html', {'jeu': jeu})


# ==========================================
# VIEW MASTER-DETAIL : DETAIL DU JEU & COMMENTAIRES
# ==========================================

def detail_jeu(request, id):
    jeu = get_object_or_404(Jeu, id=id)
    commentaires = Commentaire.objects.filter(jeu=jeu).select_related('joueur')

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            nouveau_commentaire = form.save(commit=False)
            nouveau_commentaire.jeu = jeu
            nouveau_commentaire.save()
            messages.success(request, "Votre commentaire a été publié avec succès !")
            return redirect('detail_jeu', id=jeu.id)
    else:
        form = CommentaireForm()

    return render(request, 'ludotheque/detail_jeu.html', {
        'jeu': jeu,
        'commentaires': commentaires,
        'form': form
    })
# ==========================================
# VIEWS POUR LE MODELE : JOUEUR
# ==========================================

def liste_joueurs(request):
    joueurs = Joueur.objects.prefetch_related('liste_jeux').all()
    return render(request, 'ludotheque/liste_joueurs.html', {'joueurs': joueurs})

def ajouter_joueur(request):
    if request.method == 'POST':
        form = JoueurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le profil du joueur a été créé avec succès.")
            return redirect('liste_joueurs')
    else:
        form = JoueurForm()
    return render(request, 'ludotheque/ajouter_joueur.html', {'form': form})

def modifier_joueur(request, id):
    joueur = get_object_or_404(Joueur, id=id)
    if request.method == 'POST':
        form = JoueurForm(request.POST, instance=joueur)
        if form.is_valid():
            form.save()
            messages.success(request, "Le profil du joueur a été mis à jour.")
            return redirect('liste_joueurs')
    else:
        form = JoueurForm(instance=joueur)
    return render(request, 'ludotheque/modifier_joueur.html', {'form': form, 'joueur': joueur})

def supprimer_joueur(request, id):
    joueur = get_object_or_404(Joueur, id=id)
    if request.method == 'POST':
        joueur.delete()
        messages.success(request, "Le profil du joueur a été supprimé.")
        return redirect('liste_joueurs')
    return render(request, 'ludotheque/supprimer_joueur.html', {'joueur': joueur})


# ==========================================
# VIEWS POUR LE MODELE : COMMENTAIRE
# ==========================================

def liste_commentaires(request):
    commentaires = Commentaire.objects.select_related('jeu', 'joueur').all()
    return render(request, 'ludotheque/liste_commentaires.html', {'commentaires': commentaires})

def ajouter_commentaire(request):
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le commentaire a été publié avec succès.")
            return redirect('liste_commentaires')
    else:
        form = CommentaireForm()
    return render(request, 'ludotheque/ajouter_commentaire.html', {'form': form})

def modifier_commentaire(request, id):
    commentaire_obj = get_object_or_404(Commentaire, id=id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST, instance=commentaire_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Le commentaire a été modifié.")
            return redirect('liste_commentaires')
    else:
        form = CommentaireForm(instance=commentaire_obj)
    return render(request, 'ludotheque/modifier_commentaire.html', {'form': form, 'commentaire_obj': commentary_obj})

def supprimer_commentaire(request, id):
    commentaire_obj = get_object_or_404(Commentaire, id=id)
    if request.method == 'POST':
        commentaire_obj.delete()
        messages.success(request, "Le commentaire a été supprimé.")
        return redirect('liste_commentaires')
    return render(request, 'ludotheque/supprimer_commentaire.html', {'commentaire_obj': commentaire_obj})