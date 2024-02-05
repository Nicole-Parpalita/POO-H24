import os

"""
Exercice 6:
Écrivez un programme pour écrire dans un fichier. Votre programme doit demander
le nom du fichier à utiliser et demander le texte à écrire. Une fois terminé,
votre programme doit afficher un message montrant clairement le texte provenant du fichier.
"""

i = 1
while i == 1:
    fichier = input("Quel est le nom de votre fichier ? ")
    for caractere in fichier:
        if caractere in ["?", ":", "*", "/", "|", "<", ">"]:
            print("Vous utilisez un caractère invalide.")
        else:
            pass
    if os.path.exists(fichier):
        print("Le fichier existe déjà.")
    else:
        i = 2

message = input("Quel est le message que vous voulez affichier ? ")

with open(fichier+".txt", "w") as f:
    f.write(message)

with open(fichier+".txt", "r") as f:
    print(f.read())

