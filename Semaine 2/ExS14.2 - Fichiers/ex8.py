import os
"""
Exercice 8:
Écrivez un programme qui demande le nom d'un fichier à ouvrir et affiche son contenu.
L'utilisateur pourra ainsi ajouter du contenu au fichier. Utilisez la même méthode que
l'exercice 7.
*** Note: Pour ajouter du contenu à la fin d'un fichier texte, le mode d'écriture doit être 'a'.
"""

fichier = input("Quel fichier voulez-vous ouvrir ? ")

if os.path.exists(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print("Ce fichier n'existe pas.")

demande = input("Voulez-vous ajouter du texte au fichier ? ").lower()
while True:
    if demande == "oui":
        message = input("Quel message voulez-vous ajouter ? ")
        if message != "":
            with open(fichier, "a", encoding="utf-8") as f:
                f.write(message + "\n")
            with open(fichier, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            break
    else:
        break