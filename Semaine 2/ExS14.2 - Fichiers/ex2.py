"""
Exercice 2:
Qu'arrive-t-il si on fait plus qu'une lecture à la fois?
Exécutez plusieurs lectures à la fois et notez vos observations.
"""
with open("zen.txt") as f:
    # print(f.read())
    # print(f.read())
    # print(f.read())
    # print(f.read())

    # print(f.read(12))
    # print(f.read(12))
    # print(f.read(12))
    # print(f.read(12))

    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())

    # print(f.readlines())
    # print(f.readlines())
    # print(f.readlines())
    # print(f.readlines())

    # print(f.read().splitlines())
    # print(f.read().splitlines())
    # print(f.read().splitlines())
    # print(f.read().splitlines())
    pass

"""
Notez vos observations ici:
read(): Lit le fichier juste une fois.
read(12): Lit les 12 premiers caractères et ensuite lit les 12 prochain, et ainsi de suite.
readline(): Lit une ligne à la fois selon le nombre de readline() qu'on demande (ici il lit les 4 premières lignes)
readlines(): Crée une liste de toutes les lignes du fichier incluant les \n. Crée ensuite 3 listes vides.
read().splitlines(): Crée une liste de toutes les lignes du fichier sans les \n. Crée ensuite 3 listes vides.

"""