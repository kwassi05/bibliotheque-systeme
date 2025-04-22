# src/models/emprunt.py

from datetime import date

class Emprunt:
    def __init__(self, utilisateur, livre, date_emprunt=None):
        self.utilisateur = utilisateur
        self.livre = livre
        self.date_emprunt = date_emprunt or date.today()
        self.date_retour = None
        self.statut = "En cours"

    def marquer_retour(self):
        self.date_retour = date.today()
        self.statut = "Terminé"
        self.livre.marquer_rendu()

    def __str__(self):
        return f"{self.utilisateur.nom} a emprunté '{self.livre.titre}' le {self.date_emprunt}"
