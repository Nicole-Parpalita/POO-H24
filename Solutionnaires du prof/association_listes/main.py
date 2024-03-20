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
# Ajouter auteur1 à la liste d'auteurs du livre1
livre1.lst_auteur.append(auteur1)
# Ajouter auteur1 à la liste d'auteurs du livre2
livre2.lst_auteur.append(auteur1)
# Ajouter  auteur2 à la liste d'auteurs du livre3
livre3.lst_auteur.append(auteur2)
# Afficher la liste des auteurs qui ont écrit livre1
print("\nLe(s) auteur(s) du livre1: ")
for aut in livre1.lst_auteur:
    print("-" * 35)
    print(aut)
# Afficher la liste des auteurs qui ont écrit livre2
print("\nLe(s) auteur(s) du livre2: ")
for aut in livre2.lst_auteur:
    print("-" * 35)
    print(aut)
# Afficher la liste des auteurs qui ont écrit le livre3
print("\nLe(s) auteur(s) du livre3: ")
for aut in livre3.lst_auteur:
    print("-" * 35)
    print(aut)
