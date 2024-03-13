from Classe_Personne import Personne

# Instanciation de trois instances de la classe Personne
p1 = Personne("Natalie", 19, "123456")
p2 = Personne("David", 99, "654321")
p3 = Personne("Malek")

# Méthode magique __add__
p3 + 20
p1 + 20

# Méthode magique __str__
print(p1)
print(p2)
print(p3)

# Méthode magique __len__
print("len(p1): ", len(p1))

# Méthode statique est_majeur
print("Personne.est_majeur(p1):", Personne.est_majeur(p1))

# Méthodes de classe
ls_resultat_lst = Personne.trouver_personnes_majeures_lst()
ls_resultat_dct = Personne.trouver_personnes_majeures_dict()

# Affichage des listes des personnes majeures
print("*"*50)
print("Affichage de la liste des personnes majeures 1: ")
Personne.afficher_liste(ls_resultat_lst)
print("*"*50)
print("Affichage du dictionnaire des personnes majeures 2: ")
Personne.afficher_liste(ls_resultat_dct)
print("*"*50)
