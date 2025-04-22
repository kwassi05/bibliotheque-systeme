# tests/test_emprunt.py
import unittest
from datetime import date
from models.livre import Livre
from models.utilisateur import Etudiant
from models.emprunt import Emprunt

class TestEmprunt(unittest.TestCase):
    def test_emprunt_et_retour(self):
        livre = Livre("1111111111", "1984", "George Orwell")
        etudiant = Etudiant(1, "Bob", "bob@example.com")
        emprunt = Emprunt(etudiant, livre, date(2025, 4, 17))

        self.assertTrue(livre.disponible)
        livre.marquer_emprunte()
        self.assertFalse(livre.disponible)

        etudiant.emprunter(emprunt)
        self.assertIn(emprunt, etudiant.emprunts)

        emprunt.marquer_retour()
        etudiant.rendre(emprunt)

        self.assertTrue(livre.disponible)
        self.assertEqual(emprunt.statut, "Terminé")
        self.assertNotIn(emprunt, etudiant.emprunts)

if __name__ == '__main__':
    unittest.main()
