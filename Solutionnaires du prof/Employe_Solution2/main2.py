from Classe_Employe2 import Employe


# Fonction pour déterminer l'employé prioritaire pour le stationnement gratuit
def employe_prioritaire(employe1: Employe, employe2 : Employe):
    """
     Détermine l'employé le plus prioritaire pour obtenir un stationnement gratuit
    :param employe1: le premier employé
    :param employe2: le deuxième employé
    :return: L'employé qui a la priorité ou None si non applicable
    """
    if employe1.calculer_droit_stationnement_gratuit() and employe2.calculer_droit_stationnement_gratuit():
        if employe1.calculer_anciennete() > employe2.calculer_anciennete():
            return employe1
        elif employe1.calculer_anciennete() < employe2.calculer_anciennete():
            return employe2
    return None


if __name__ == "__main__":

    # Instantioation d'un employé
    employe = Employe()
    # Saisie des informations de l'employé
    # Saisie et validation du matricule
    while True:
        try:
            matricule = input("Entrez le matricule de l'employé (7 chiffres) : ")
            employe.matricule = matricule
            break
        except ValueError as e:
            print(f"Erreur : {e}")
    # Saisie et validation du nom
    while True:
        try:
            nom = input("Entrez le nom de l'employé : ")
            employe.nom = nom
            break
        except ValueError as e:
            print(f"Erreur : {e}")
    # Saisie et validation du prénom
    while True:
        try:
            prenom = input("Entrez le prénom de l'employé : ")
            employe.prenom = prenom
            break
        except ValueError as e:
            print(f"Erreur : {e}")
    # Saisie et validation de l'année de naissance
    while True:
        try:
            annee_naissance = int(input("Entrez l'année de naissance de l'employé : "))
            employe.annee_naissance = annee_naissance
            break
        except ValueError:
            print("Veuillez entrer une année valide.")

    # Saisie et validation du salaire annuel
    while True:
        try:
            salaire_annuel = float(input("Entrez le salaire annuel de l'employé : "))
            employe.salaire_annuel = salaire_annuel
            break
        except ValueError:
            print("Veuillez entrer un montant valide pour le salaire annuel(<=70000).")

    # Saisie et validation de l'année d'entrée en fonction
    while True:
        try:
            annee_entree_fonction = int(input("Entrez l'année d'entrée en fonction de l'employé : "))
            employe.annee_entree_fonction = annee_entree_fonction
            break
        except ValueError:
            print("Veuillez entrer une année valide.")

    # Affichage des informations de l'employé
    #employe.afficher_informations()
    print(employe)

    # Fonction Employe_prioritaire()
    employe_ = Employe("1234568", "nom-employe", "prenom-employe", 2000, 20000, 2024)

    print("L'employé qui a le droit au stationnement gratuit est : ", employe_prioritaire(employe, employe_))






