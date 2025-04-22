# src/models/utilisateur.py

class Utilisateur:
    def __init__(self, id_utilisateur, nom, email):
        self.id_utilisateur = id_utilisateur
        self.nom = nom
        self.email = email
        self.emprunts = []

    def emprunter(self, emprunt):
        self.emprunts.append(emprunt)

    def rendre(self, emprunt):
        if emprunt in self.emprunts:
            self.emprunts.remove(emprunt)


class Etudiant(Utilisateur):
    pass


class Enseignant(Utilisateur):
    pass


class Bibliothecaire:
    def __init__(self, identifiant):
        self.identifiant = identifiant
