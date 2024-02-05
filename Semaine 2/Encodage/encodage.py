import sys
import random


def afficher_menu() -> str:
    """
    Affiche le menu et retourne le choix de l'utilisateur
    :return: Le choix de l'utilisateur
    """
    choix = print("""\nBienvenue au système d'encodage !

Souhaitez-vous : 
1. Encoder un mot 
2. Encoder une phrase
3. Deviner un mot
0. Quitter le programme.
""")
    return choix


def encoder_mot(ls_lettres: list) -> int:
    """
    Demander un mot à encoder. Rechercher les nombres associés à chaque lettre puis les aditionner.
    :param ls_lettres: La liste des lettres et de leurs valeurs.
    :return: Le mot encodé
    """
    valeur_mot = 0

    while True:
        mot = input("Entrez un mot que vous voulez encoder: ").upper()
        for caractere in mot:
            if caractere.isalpha() or caractere in [" "]:
                for paire in ls_lettres:
                    if paire[0] == caractere:
                        valeur_mot += paire[1]
            else:
                print("Le mot ne peut être composé que de lettres.")
                sys.exit()
        break

    return valeur_mot


def encoder_phrase(ls_lettres: list) -> str:
    """
    Demande une phrase à encoder. Recher les valeurs des lettres et affiche le code numérique.
    :param ls_lettres: La liste des lettres et de leurs valeurs.
    :return: La phrase encodée
    """

    ls_phrase = []


    while True:
        valeur_mot = 0
        phrase = input("Entrez une phrase que vous voulez encoder: ").upper()
        mots = phrase.split()

        for mot in mots:
            for caractere in mot:
                if caractere.isalpha() or caractere in [" "]:
                    for paire in ls_lettres:
                        if paire[0] == caractere:
                            valeur_mot += paire[1]
                else:
                    print("Le mot ne peut être composé que de lettres.")
                    sys.exit()
            ls_phrase.append(valeur_mot)

        resultat_encodage = ", ".join(map(str, ls_phrase))
        return resultat_encodage
        break


def deviner_mot(ls_lettres: list) -> bool:
    """
    Donne un chiffre aléatoirement et demande à l'utilisateur de le deviner un mot correspondant.
    :param ls_lettres: La liste des lettres et de leur valeurs
    :return: True si le mot est deviné, False si non
    """
    valeur_mot = 0

    while True:
        chiffre_aleatoire = random.randint(1, 800)
        print(f"Le chiffre aléatoire généré est de: {chiffre_aleatoire}.")

        devinette = input("Quel mot pensez-vous qui correspond à ce chiffre ? ").upper()
        for caractere in devinette:
            if caractere.isalpha() or caractere in [" "]:
                for paire in ls_lettres:
                    if paire[0] == caractere:
                        valeur_mot += paire[1]
            else:
                print("Le mot ne peut être composé que de lettres.")
                sys.exit()
        if valeur_mot == chiffre_aleatoire:
            return True
        else:
            return False

        break



def encodage():
    ls_lettres = [["A", 1], ["B", 2], ["C", 3], ["D", 4], ["E", 5], ["F", 6],
                  ["G", 7], ["H", 8], ["I", 9], ["J", 10], ["K", 20], ["L", 30],
                  ["M", 40], ["N", 50], ["O", 60], ["P", 70], ["Q", 80], ["R", 90],
                  ["S", 100], ["T", 200], ["U", 300], ["V", 400], ["W", 500],
                  ["X", 600], ["Y", 700], ["Z", 800], [" ", 900]]


    while True:
        afficher_menu()
        choix = input("Votre choix: ")
        if choix == "1":
            valeur_mot = encoder_mot(ls_lettres)
            print(f"La valeur de votre mot est : {valeur_mot}.")
        elif choix == "2":
            phrase_encodee = encoder_phrase(ls_lettres)
            print(f"Votre phrase encodée est: {phrase_encodee}")
        elif choix == "3":
            resultat = deviner_mot(ls_lettres)
            if resultat == True:
                print("Félicitations! Vous avez deviné un bon mot!")
            else:
                print("Le mot que vous avez deviné n'est pas équivalent au chiffre aléatoire.")
        elif choix == "0":
            print("\nMerci d'avoir utilisé notre service, à bientôt !")
            break
        else:
            print("\nChoix invalide, essayez de nouveau.")



if __name__ == "__main__":
    encodage()
