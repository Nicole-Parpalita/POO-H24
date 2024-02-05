"""
Exercice 5:
Réparez les problèmes vus dans les exercices précédents.
"""

# EX3
with open("sortie_ex5_3.txt", "w") as f:
    f.write("Ligne 1\n")
    f.write("Ligne 2\n")
    f.write("Ligne 3\n")
    f.write("Ligne 4")


# EX4
lst_lignes = [
    'Ligne 1\n',
    'Ligne 2\n',
    'Ligne 3\n',
    'Ligne 4'
]
with open("sortie_ex5_4.txt", "w") as f:
    f.writelines(lst_lignes)
