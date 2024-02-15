from Classe_Compte import Compte
import sys

# Fonction pour calculer le total des soldes de deux comptes appartenant au même client
def calculer_total(compte: Compte, compte2: Compte):
    """
    Calculer le total des soldes de deux comptes appartenant au même client.
    :param compte: Le premier compte du client
    :param compte2: Le deuxième compte du client
    :return: Le total des soldes des deux comptes
    """
    if compte.nom_prenom_client == compte2.nom_prenom_client:
        solde_total = compte.solde_compte + compte2.solde_compte
        return solde_total
    else:
        return -1

if __name__ == '__main__':

    # Instanciation d'un compte
    compte = Compte()

    # Saisie des informations du compte
    # Saisie et validation du numéro de compte
    while True:
        try:
            num_compte = input("Entrez le numéro de compte (10 caractères): ")
            compte.num_compte = num_compte
            break
        except ValueError:
            print(f"S'il vous plaît entrer une numéro de compte valide.")

    # Saisie et validation du nom et prénom du client
    while True:
        try:
            nom_prenom_client = input("Entrez le nom et le prénom du client: ")
            compte.nom_prenom_client = nom_prenom_client
            break
        except ValueError:
            print(f"S'il vous plaît entrer un nom et prénom valide.")

    # Saisie et validation du type de compte
    while True:
        try:
            type_compte = input("Entrez le type de compte (chèque ou épargne): ").capitalize()
            compte.type_compte = type_compte
            break
        except ValueError:
            print(f"S'il vous plaît entrer un type de compte valide.")

    # Saisie et validation du solde du compte
    while True:
        try:
            solde_compte = float(input("Entrez le solde du compte: "))
            compte.solde_compte = solde_compte
            break
        except ValueError:
            print(f"S'il vous plaît entrer un solde de compte valide.")


    # Créer un deuxième compte qui est instancié directement dans le code
    compte2 = Compte("A123456789", "Nicole Parpalita", "Épargne",
                     2250.50)

    # Déposer de l'argent dans les deux comptes créés
    while True:
        try:
            depot1 = float(input(f"\nQuelle quantité voulez vous déposer dans votre premier compte? Solde actuel: "
                                 f"{compte.solde_compte} $. Quantité: "))
            if depot1 == "":
                break
            compte.solde_compte = compte.deposer(depot1)
            break
        except ValueError:
            print("Le dépôt doit être une quantité d'argent.")

    while True:
        try:
            depot2 = float(input(f"\nQuelle quantité voulez vous déposer dans votre deuxième compte? Solde actuel: "
                                 f"{compte2.solde_compte} $. Quantité: "))
            if depot2 == "":
                break
            compte2.solde_compte = compte2.deposer(depot2)
            break
        except ValueError:
            print("Le dépôt doit être une quantité d'argent.")

    # Retirer de l'argent du premier compte
    while True:
        try:
            retrait = float(input(f"\nQuelle quantité voulez-vous retirer de votre premier compte? Solde actuel: "
                                 f"{compte.solde_compte} $. Quantité: "))
            compte.solde_compte = compte.retirer(retrait)
            break
        except ValueError:
            print("Votre compte doit avoir 100$ à l'intérieur à tout temps.")

    # Calculer le total des soldes des deux comptes
    solde_total = calculer_total(compte, compte2)

    # Afficher le nombre d'instances de la classe Compte créés
    nb_instances = Compte.nb_comptes
    print(f"\n{nb_instances} comptes ont été créés.")

    # Sauvegarder toutes les informations des deux comptes dans un fichier texte
    try:
        with open("Informations_comptes.txt", "a", encoding = "utf-8") as f:
            f.write(f"{Compte.afficher_informations(compte)}")
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
        sys.exit()

    try:
        with open("Informations_comptes.txt", "a", encoding = "utf-8") as f:
            f.write(f"{Compte.afficher_informations(compte2)}")
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
        sys.exit()


