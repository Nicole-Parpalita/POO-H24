import os
"""
Exercice 7:
Modifiez le programme de l'exercice 6 afin de permettre d'écrire plusieurs lignes.
Pour se faire, vous devrez demander des lignes jusqu'à ce que le texte soit égal à EOF.
Vous devez également utiliser une liste pour stocker chaque ligne de texte.
Finalement, affichez le contenu du fichier à l'utilisateur clairement.
"""

ls_texte = []

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

message = input("Quel est le message que vous voulez afficher (espace si rien) ? ")
ls_texte.append(message)

while True:
    if message != "":
        message = input("Quel est le message que vous voulez affichier ? ")
        ls_texte.append(message)
    else:
        break

with open(fichier, "w", encoding= "utf-8") as f:
    for element in ls_texte:
        f.write(element + "\n")

with open(fichier, "r", encoding= "utf-8") as f:
    print(f.read())


