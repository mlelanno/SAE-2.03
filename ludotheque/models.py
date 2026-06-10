from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField()

    def __str__(self):
        return self.nom

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        if self.prenom:
            return f"{self.prenom} {self.nom}"
        return self.nom

class Jeu(models.Model):
    titre = models.CharField(max_length=200)
    annee_sortie = models.IntegerField()
    editeur = models.CharField(max_length=100)
    
    # THE NEW VISUAL ASSET FIELD
    image_url = models.URLField(max_length=500, blank=True, null=True)
    
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mail = models.EmailField()
    mot_de_passe = models.CharField(max_length=100)
    
    CHOIX_TYPE = [
        ('pro', 'Professionnel'),
        ('part', 'Particulier'),
    ]
    type_joueur = models.CharField(max_length=10, choices=CHOIX_TYPE)
    liste_jeux = models.ManyToManyField(Jeu, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Commentaire(models.Model):
    jeu = models.ForeignKey(Jeu, on_delete=models.CASCADE)
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    note = models.IntegerField() 
    commentaire = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.note}/20 by {self.joueur} on {self.jeu}"