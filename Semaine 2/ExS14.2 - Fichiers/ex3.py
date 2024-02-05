"""
Exercice 3:
Avant d'exécuter, lisez le code et émettez une hypothèse. Exécutez le code et vérifiez votre réponse.
Y a-t-il des différences entre votre hypothèse et le résultat?
"""
with open("sortie_ex3.txt", "w") as f:
    f.write("Ligne 1")
    f.write("Ligne 2")
    f.write("Ligne 3")
    f.write("Ligne 4")

"""
Hypothèse: Il va créer le fichier sortie_ex3.txt et il sera afficher Ligne 4.
Observation: Il écrit chaque chaîne envoyée et elles sont collées dans la même ligne.    
"""