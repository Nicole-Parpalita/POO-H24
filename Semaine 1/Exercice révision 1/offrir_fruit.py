from datetime import datetime
import random

fruits = {
    "pomme": 1.50,
    "banane": 0.75,
    "orange": 1.20,
    "fraise": 2.00,
    "kiwi": 1.80
    }

def verifier_nom_de_famille(nom_de_famille: str) -> bool:
    """
    Vérifier que le nom de famille est conforme aux conditions
    :param nom_de_famille: Le nom de famille
    :return: Le nom de famille validé
    """
    # Vérifier que le nom de famille a au moins 3 lettres de longueur
    if len(nom_de_famille) > 3:
        nom_de_famille = nom_de_famille
    else:
        print("Le nom de famille est trop court.")
        return None

    # Vérifier que le nom de famille contient seulement des lettres, des espaces, des tirets et des apostrophes
    for caractere in nom_de_famille:
        if caractere.isalpha() or caractere in [" ", "-", "'"]:
            continue
        else:
            print("Le nom de famille doit seulement contenir des lettres, des espaces, des tirets ou des apostrophes.")
            return None
        break
    return nom_de_famille

def verifier_date_de_naissance(jour_de_naissance: int, mois_de_naissance: int, annee_de_naissance: int) -> str:
    """
    Vérifier que la date de naissance respecte la structure JJ-MM-AAAA
    :param jour_de_naissance: Le jour de naissance du client
    :param mois_de_naissance: Le mois de naissance du client
    :param annee_de_naissance: L'année de naissance du client
    :return: La date de naissance du client sous la structure JJ-MM-AAAA
    """
    # Vérifier l'année de naissance
    if annee_de_naissance > 2024:
        print("Cette année n'existe pas encore.")
        return None
    else:
        annee_de_naissance = str(annee_de_naissance)


    # Vérifier le mois de naissance
    if mois_de_naissance < 1 or mois_de_naissance > 12:
        print("Ce mois de naissance est invalide.")
        return None
    else:
        mois_de_naissance = str(mois_de_naissance)


    # Vérifier le jour de naissance
    if jour_de_naissance < 1 or jour_de_naissance > 31:
        print("Ce jour de naissance est invalide.")
        return None
    else:
        jour_de_naissance = str(jour_de_naissance)


    # Construire la date de naissance
    date_de_naissance = f"{jour_de_naissance}-{mois_de_naissance}-{annee_de_naissance}"

    return date_de_naissance


def calculer_age(annee_de_naissance) -> str:
    """
    Calculer l'âge du client
    :param annee_de_naissance: L'année de naissance du client
    :return: L'âge du client
    """
    # Identifier la date actuelle
    date_actuelle = datetime.now()
    annee_actuelle = int(date_actuelle.strftime("%Y"))

    # Calculer l'âge du client
    age_client = annee_actuelle - annee_de_naissance

    return age_client

def verifier_gagnant(age_client: int, dt_fruits: dict, date_de_naissance: str, nom_de_famille: str) -> str:
    """
    Vérifier que le client a 70 ans et qu'il peut obtenir un fruit gratuit et créer le dict du client gagnant
    :param age_client: L'âge du client
    :return: Le dictionnaire du client gagnant, ou rien
    """
    # Vérifier si le client est canditat ou non et trouver un fruit aléatoirement
    if age_client < 70:
        print("\nVous ne pouvez pas obtenir un fruit gratuit. Désolé.")
    else:
        fruit = random.choice(list(dt_fruits.keys()))
        dt_gagnant = {}
        dt_gagnant = {"Nom de famille": nom_de_famille, "Âge": age_client, "Date de naissance": date_de_naissance,
                      "Fruit gagné": fruit}
        return dt_gagnant



# Boucle principale
dt_client_gagnant = {}

# Demander le nom de famille au client
nom_de_famille = input("Quel est votre nom de famille ? ").capitalize()

# Vérifier que le nom de famille est valide
nom_de_famille_valide = verifier_nom_de_famille(nom_de_famille)
while True:
    if nom_de_famille_valide == None:
        nom_de_famille = input("Quel est votre nom de famille ? ").capitalize()
        nom_de_famille_valide = verifier_nom_de_famille(nom_de_famille)
    else:
        break

# Établir la date de naissance du client
# Année
while True:
    try:
        annee_de_naissance = int(input(f"\nQuel est votre année de naissance ? "))
        break
    except ValueError:
        print("Cette année est invalide.")

# Mois
while True:
    try:
        mois_de_naissance = int(input(f"\nQuel est votre mois de naissance ? "))
        break
    except ValueError:
        print("Ce mois est invalide.")

# Jour
while True:
    try:
        jour_de_naissance = int(input(f"\nQuel est votre jour de naissance ? "))
        break
    except ValueError:
        print("Ce jour est invalide.")



# Assurer que la date de naissance respecte la structure JJ-AA-MMMM
date_de_naissance = verifier_date_de_naissance(jour_de_naissance, mois_de_naissance, annee_de_naissance)


# Calculer l'âge du client
age_client = calculer_age(annee_de_naissance)

# Vérifier si le client peut gagner un fruit aléatoire et créer son dictionnaire
gagnant = verifier_gagnant(age_client, fruits, date_de_naissance, nom_de_famille_valide)
print(gagnant)
print(f"\nFélicitations ! Vous avez gagné un fruit gratuit.")
