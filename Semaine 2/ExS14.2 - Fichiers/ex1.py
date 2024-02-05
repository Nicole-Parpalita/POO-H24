"""
Exercice 1:
Dans cet exercice, vous devez expliquer les différences entre
les différentes fonctions de lecture de texte à partir d'un fichier.
ATTENTION! Ne pas exécuter toutes les lignes d'un coup. Enlever un commentaire à la fois.
"""
with open("zen.txt") as f:
    # print(f.read())
    # print(f.read(12))
    # print(f.readline())
    # print(f.readlines())
    # print(f.read().splitlines())
    pass

"""
Écrire une brève description de chaque fonction ici
f.read():               Ça lit l'entièreté du fichier.
f.readline():           Ça lit la première ligne du fichier.
f.readlines():          Ça crée une liste de toutes les lignes du fichier. Ça lit la incluant les \n.
f.read(12):             Ça lit les 12 premiers caractères du fichier.
f.read().splitlines():  Ça crée une liste de toutes les lignes dy fichier sans les \n.
"""