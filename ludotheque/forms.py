from django import forms
from .models import Auteur

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['nom', 'prenom', 'age']