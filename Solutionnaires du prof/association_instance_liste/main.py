from classe_auteur import Auteur
from classe_livre import Livre
# Instancier trois livres
livre1 = Livre("1234567891234", "L'alchimiste")
livre2 = Livre("154125233333", "Le pélerin de compostelle")
livre3 = Livre("9876543219876","Apprendre à programmer avec Python 3")
# Instancier deux auteurs
auteur1 = Auteur("123456", "Paulo", "Coelho", [livre1, livre2])
auteur2 = Auteur("654321", "Swinnen", "Gérard")
auteur2.lst_livres.append(livre3)

# Afficher tous les livres écrits par auteur1
print("\nLe(s) livre(s) écrit(s) par auteur1: ")
for lvr in auteur1.lst_livres:
    print("-" * 35)
    print(lvr)

# Afficher tous les livres écrits par auteur2
print("\nLe(s) livre(s) écrit(s) par auteur2: ")
for lvr in auteur2.lst_livres:
    print("-" * 35)
    print(lvr)
# Assigner auteur1 à l'attribut auteur du livre1
livre1.auteur = auteur1
# Assigner auteur1 à l'attribut auteur du livre2
livre2.auteur = auteur1
# Assigner auteur2 à l'attribut auteur du livre3
livre3.auteur = auteur2
# Afficher l'auteur du livre1
print("\nL'auteur du livre1: ")
print("-" * 35)
print(livre1.auteur)
# Afficher l'auteur du livre2
print("\nL'auteur du livre2: ")
print("-" * 35)
print(livre2.auteur)
# Afficher l'auteur du livre3
print("\nL'auteur du livre3: ")
print("-" * 35)
print(livre3.auteur)

