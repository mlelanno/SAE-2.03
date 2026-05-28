from django import forms
from .models import Auteur, Categorie, Jeu, Joueur, Commentaire

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['nom', 'prenom', 'age']

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom', 'descriptif']

class JeuForm(forms.ModelForm):
    class Meta:
        model = Jeu
        fields = ['titre', 'annee_sortie', 'editeur', 'auteur', 'categorie']

class JoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = ['nom', 'prenom', 'mail', 'mot_de_passe', 'type_joueur', 'liste_jeux']
        widgets = {
            'liste_jeux': forms.CheckboxSelectMultiple(),
            'mot_de_passe': forms.PasswordInput(),
        }

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['jeu', 'joueur', 'note', 'commentaire']
        widgets = {
            # Blocage de la note entre 0 et 20 directement dans le formulaire HTML
            'note': forms.NumberInput(attrs={'min': 0, 'max': 20, 'class': 'form-control'}),
            'commentaire': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }