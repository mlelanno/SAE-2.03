from django.shortcuts import render, redirect
from .models import Auteur
from .forms import AuteurForm

def liste_auteurs(request):
    auteurs = Auteur.objects.all()
    return render(request, 'ludotheque/liste_auteurs.html', {'auteurs': auteurs})

def ajouter_auteur(request):
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_auteurs')
    else:
        form = AuteurForm()
    return render(request, 'ludotheque/ajouter_auteur.html', {'form': form})