# SAE 2.03 / 2.13 - Systeme de Gestion de Ludotheque

## Description du Projet
Ce repertoire contient le code source du systeme de gestion de ludotheque developpe dans le cadre du BUT Reseaux et Telecommunications. L'application est concue pour gerer le cycle de vie complet d'une bibliotheque de jeux, en separant strictement les environnements de developpement et de production pour eviter toute derive de configuration.

## Architecture Technique
- Cadre applicatif (Framework) : Django (Python 3)
- Bases de donnees :
  - Developpement : SQLite3 (base locale embarquee)
  - Production : MariaDB (base relationnelle robuste)
- Front-end : HTML5, CSS3 (Mode sombre natif), Bootstrap
- Securite : Protection native contre les injections SQL via l'ORM Django, validation systematique des jetons CSRF, et isolation des variables d'environnement.

## Fonctionnalites Principales
- Operations CRUD : Interface unifiee pour la creation, lecture, modification et suppression des entites (Jeux, Auteurs, Categories, Joueurs, Commentaires).
- Integrite relationnelle : Gestion des liaisons ForeignKey et ManyToMany avec protocoles de suppression en cascade.
- Importation de donnees : Module d'importation CSV integre pour l'ajout massif et automatise de categories et de jeux.

## Deploiement Local (Developpement)

1. Clonage du repertoire distant :
git clone https://github.com/mlelanno/SAE-2.03.git
cd SAE-ARNAULT

2. Creation et activation de l'environnement virtuel :
python -m venv venv --copies
.\venv\Scripts\Activate.ps1

3. Installation des dependances :
pip install -r requirements.txt

4. Configuration :
Creer un fichier .env a la racine avec vos identifiants locaux. Ce fichier ne doit jamais etre pousse sur Git.

5. Initialisation de la base locale :
python manage.py migrate

6. Lancement du daemon local :
python manage.py runserver

## Deploiement en Production (Serveur Debian)

1. Etablissement du tunnel SSH :
ssh martin@10.128.208.51

2. Rapatriement du code source :
cd SAE-ARNAULT
git pull origin main

3. Lancement du service applicatif :
source venv/bin/activate
sudo venv/bin/python manage.py runserver 0.0.0.0:80

## Auteurs
- Martin Le Lanno : Architecture Backend, Versioning, UI/UX et Resolution d'anomalies
- Metehan : Administration de Base de Donnees et Configuration du Serveur de Production
