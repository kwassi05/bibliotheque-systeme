# src/models/livre.py
class Livre:
    def __init__(self, isbn, titre, auteur):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def __str__(self):
        return f"{self.titre} par {self.auteur} (ISBN: {self.isbn})"

    def marquer_emprunte(self):
        self.disponible = False

    def marquer_rendu(self):
        self.disponible = True
