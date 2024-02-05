import random

tpl_lettres = (('A','B','C','D','E','F','G','H','I'),   #tpl_lettres[0]
               ('J','K','L','M','N','O','P','Q','R'),   #tpl_lettres[1]
               ('S','T','U','V','W','X','Y','Z'))       #tpl_lettres[2]

#fonction pour uniformiser : ôter les accents.
#paramèetre : le mot à uniformiser
#retourne le mot sans les accents
def uniformiser(mot):
    mot = mot.lower()
    mot = mot.replace("æ", "ae")
    mot = mot.replace("œ", "oe")
    accents = "èêéëàâäáîïíìôòóöùüûúÿýŷỳç"  # caractères à remplacer
    lettres = "eeeeaaaaiiiioooouuuuyyyyc"  # caractères de remplacements, avec les mêmes indices (mêmes positions)
    for i in range(0, len(accents)):
        mot = mot.replace(accents[i], lettres[i])  # boucle pour remplacer tous les accents par des lettres normales
    return mot

#fonction pour encoder un mot
#paramètre : le mot à encoder
#retourne le code correspondant au mot
def encoder(mot):
    code = 0
    mot = uniformiser(mot) # enlever les accents.
    mot = mot.upper()
    for c in mot:
        if c in tpl_lettres[0]:                     #si la lettre est dans la première ligne
            code += tpl_lettres[0].index(c)+1       #on ajoute un à l'indice de la lettre.
        elif c in tpl_lettres[1]:                   #si c'est dans la 2e ligne
            code += (tpl_lettres[1].index(c)+1)*10  #on ajoute 1 et on multiplie par 10
        elif c in tpl_lettres[2]:
            code += (tpl_lettres[2].index(c) + 1) * 100
    return code

#fonction pour encoder une liste de mots
#paramètre : la liste de mots à encoder
#retourne une liste de codes correspondants aux mots
def encoderListe(liste):
    ls_codes = []  # à optimiser
    for mot in liste:
        ls_codes.append(encoder(mot))
    return ls_codes

# menu principal
while True :
    choix = input("Voulez-vous encoder un MOT, une LISTE de mot, une PHRASE, ou jouer aux DEVINETTE? ").upper()
    if choix == "MOT":
        mot = input("Entrez le mot à encoder : ")
        print("Le code est : ", encoder(mot))
    elif choix == "LISTE":
        ls_mots = []
        while True:
            mot = input("Entrer le prochain mot à encoder ou ENTER pour terminer : ")
            if mot == "":
                break
            ls_mots.append(mot)
        ls_codes = encoderListe(ls_mots)
        print("Les codes sont:", ls_codes)
    elif choix == "PHRASE":
        phrase = input("Entrer la phrase : ")
        ls_mots = phrase.split(" ")
        ls_codes = encoderListe(ls_mots)
        print("Les codes sont:", ls_codes)
    elif choix == "DEVINETTE":
        code = random.randint(0,1000)
        while True:
            mot = input("Entrer un mot pour le code " + str(code) + " : ")
            if encoder(mot) == code:
                print("Bravo")
                break
            else:
                print("Essaye encore")
    else:
        break
