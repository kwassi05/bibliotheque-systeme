# src/main.py

from models.livre import Livre
from models.utilisateur import Etudiant
from models.emprunt import Emprunt

# Création d'un livre
livre1 = Livre("1234567890", "Le Petit Prince", "Antoine de Saint-Exupéry")

# Création d'un utilisateur
etudiant1 = Etudiant(1, "Alice", "alice@example.com")

# Création d'un emprunt
emprunt1 = Emprunt(etudiant1, livre1)

# Marquer le livre comme emprunté
livre1.marquer_emprunte()

# Ajouter l'emprunt à l'utilisateur
etudiant1.emprunter(emprunt1)

# Afficher les infos
print(emprunt1)

# Marquer le retour
emprunt1.marquer_retour()
etudiant1.rendre(emprunt1)

print(f"Retour effectué pour : {livre1.titre}, disponible : {livre1.disponible}")
