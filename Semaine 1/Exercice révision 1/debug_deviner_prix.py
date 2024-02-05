import random

# Dictionnaire des produits (fruits) avec leurs prix
fruits = {
    "pomme": 1.50,
    "banane": 0.75,
    "orange": 1.20,
    "fraise": 2.00,
    "kiwi": 1.80
}


def afficher_menu():
    """
    Affiche le menu du programme
    :return: None
    """
    print("\nMenu :")
    print("1. Jouer au jeu Devine le Prix")
    print("2. Ajouter un fruit et son prix")
    print("3. Modifier le prix d'un fruit existant")
    print("4. Afficher la liste des fruits et leurs prix")
    print("5. Quitter")


def ajouter_fruit():
    """
    Ajoute et affiche le fruit entré dans le dictionnaire
    s'il n'existe pas déjà.
    :return: None
    """
    fruit = input("Entrez le nom du fruit à ajouter : ").lower()
    if fruit in fruits:
        print("Ce fruit existe déjà. Utilisez l'option pour modifier le prix.")
    else:
        try:
            prix = float(input(f"Entrez le prix de {fruit.capitalize()} : "))
            if prix < 0:
                print("Le prix doit être positif.")
                return
            fruits[fruit] = prix
            print(f"{fruit.capitalize()} a été ajouté à la liste avec un prix de {prix} $.")
        except ValueError:
            print("Le prix doit être un nombre réel positif.")


def modifier_prix():
    """
    Modifie et affiche le prix du fruit si le fruit existe dans le dictionnaire
    :return: None
    """
    print("Liste des fruits actuels :")
    for fruit, prix in fruits.items():
        print(f"- {fruit.capitalize()}     : {prix} $")

    fruit_modif = input("Entrez le nom du fruit à modifier : ").lower()
    if fruit_modif in fruits:
        try:
            nouveau_prix = float(input(f"Entrez le nouveau prix de {fruit_modif.capitalize()} : "))
            if nouveau_prix < 0:
                print("Le prix doit être positif.")
                return
            else:
                fruits[fruit_modif] = nouveau_prix
                print(f"Le prix de {fruit_modif.capitalize()} a été modifié avec succès à {nouveau_prix} $.")
        except ValueError:
            print("Le prix doit être un nombre réel positif.")
    else:
        print("Ce fruit n'existe pas. Veuillez ajouter le fruit d'abord.")
        

def deviner_prix():
    """
    Choisit un fruit aléatoirement et permet à l'utilisateur
    de faire 3 essais pour deviner son prix
    :return: True si le prix a été deviné et False sinon
    """
    choix_fruit = random.choice(list(fruits.keys()))
    prix_correct = fruits[choix_fruit]

    print("\nBienvenue dans le jeu Devine le Prix !")
    print("Un fruit a été choisi au hasard. Devinez le prix !")
    print(f"Le fruit choisi est : {choix_fruit.capitalize()}")

    essais = 3
    while essais > 0:
        try:
            devine = float(input("Entrez votre estimation du prix du fruit : "))
            if devine == prix_correct:
                print("Vous avez deviné le bon prix.")
                return True
            else:
                if devine < prix_correct:
                    print("Le prix est plus élevé !")
                else:
                    print("Le prix est plus bas !")
                essais -= 1
                print(f"Il vous reste {essais} essais.")
        except ValueError:
            print("Veuillez entrer un nombre valide pour le prix.")

    print(f"Le prix correct était : {prix_correct} $. Vous avez épuisé tous vos essais.")
    return False

# Programme principal
while True:
    afficher_menu()
    choix = input("Entrez votre choix : ")

    if choix == '1':
        resultat = deviner_prix()
        if resultat is True :
            print("Bravo !")
        else:
            print("Essaye encore !")
    elif choix == '2':
        ajouter_fruit()
    elif choix == '3':
        modifier_prix()
    elif choix == '4':
        print("\nListe des fruits et de leurs prix actuels :")
        for fruit, prix in fruits.items():
            print(f"- {fruit.capitalize()} : {prix} $")
    elif choix == '5':
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez entrer un numéro de choix valide.")
