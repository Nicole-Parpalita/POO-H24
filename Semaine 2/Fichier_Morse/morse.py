import sys

fichier_traduit = "phrase_traduite.txt"

def traduire_dict() -> dict:
    """
    Traduire un fichier texte en dictionnaire
    return: Le dictionnaire contenant le code morse
    """
    dict_morse = {}
    try:
        with open("morse.txt", "r", encoding= "utf-8") as f:
            for ligne in f:
                cle, valeur = ligne.strip().split(";")
                dict_morse[cle] = valeur
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
        sys.exit()

    return dict_morse

def traduire_phrase(dict_morse: dict) -> list:
    """
    Traduire une phrase en code morse
    dict_morse: Le dictionnaire du code morse
    return: La liste des caractères traduits de la phrase en code morse
    """
    ls_phrase = []
    while True:
        phrase = input("Entrez une phrase que vous voulez traduite en code morse: ").upper()
        for caractere in phrase:
            if caractere == " ":
                print("Vous n'avez pas le droit à mettre des espaces.")
        break
    for caractere in phrase:
        ls_phrase.append(dict_morse[caractere])

    return ls_phrase


# Programme principale

dict_morse = traduire_dict()
ls_phrase = traduire_phrase(dict_morse)

try:
    with open(fichier_traduit, "w", encoding= "utf") as f:
        f.writelines(ls_phrase)
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé.")
    sys.exit()


try:
    with open(fichier_traduit, "r", encoding= "utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé.")
    sys.exit()
